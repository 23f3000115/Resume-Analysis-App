from flask import Flask, request, render_template, jsonify, send_file
import os
from werkzeug.utils import secure_filename
from resume_parser import extract_text_from_pdf
from scoring import analyze_resume, extract_skills_from_text, compare_with_job_title
from ai_services import generate_summaries, rewrite_sentence_suggestions, ats_preview

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('file')
    if not f:
        return jsonify({'error': 'No file uploaded'}), 400
    filename = secure_filename(f.filename)
    if not filename.lower().endswith('.pdf'):
        return jsonify({'error': 'Only PDF files allowed'}), 400
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    f.save(path)
    text = extract_text_from_pdf(path)
    skills = extract_skills_from_text(text)
    score, details = analyze_resume(text, skills)
    return jsonify({'text': text, 'skills': skills, 'score': score, 'details': details})

@app.route('/generate_summaries', methods=['POST'])
def generate_summaries_route():
    data = request.json or {}
    highlights = data.get('highlights', '')  
    options = generate_summaries(highlights)
    return jsonify({'options': options})

@app.route('/rewrite', methods=['POST'])
def rewrite():
    data = request.json or {}
    sentence = data.get('sentence', '')
    suggestions = rewrite_sentence_suggestions(sentence)
    return jsonify({'suggestions': suggestions})

@app.route('/job_compare', methods=['POST'])
def job_compare():
    data = request.json or {}
    resume_text = data.get('resume_text', '')
    job_title = data.get('job_title', '')
    matches, gaps = compare_with_job_title(resume_text, job_title)
    return jsonify({'matches': matches, 'gaps': gaps})

@app.route('/ats_preview', methods=['POST'])
def ats_preview_route():
    resume_text = (request.json or {}).get('resume_text', '')
    preview = ats_preview(resume_text)
    return jsonify({'preview': preview})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
