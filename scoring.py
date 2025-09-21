import re
from collections import Counter

# Basic skill extraction heuristics (can be replaced by spaCy / NER)
COMMON_SKILLS = ['python','java','c++','c#','javascript','react','node','django','flask','sql','aws','azure','docker','kubernetes','git','excel','powerpoint']

def extract_skills_from_text(text):
    text_low = text.lower()
    found = set()
    for skill in COMMON_SKILLS:
        if re.search(r'\\b' + re.escape(skill) + r'\\b', text_low):
            found.add(skill)
    # Also extract all capitalized words that look like technologies (quick heuristic)
    caps = re.findall(r'\\b[A-Z][A-Za-z0-9+#\\.\\-]{1,30}\\b', text)
    for c in caps:
        if len(c) > 1 and c.lower() not in found:
            found.add(c)
    return sorted(list(found))

def analyze_resume(text, skills):
    # Score out of 10 across multiple criteria (simple heuristics)
    sections = {
        'contact': bool(re.search(r'email|@|phone|tel', text, re.I)),
        'experience': bool(re.search(r'experience|worked|responsibilities|projects', text, re.I)),
        'education': bool(re.search(r'education|university|college|bachelor|master|phd', text, re.I)),
    }
    completeness = sum(sections.values()) / len(sections)

    # Clarity: penalize very long sentences (heuristic)
    sentences = re.split(r'[\\.!?]+', text)
    avg_len = sum(len(s.split()) for s in sentences if s.strip()) / max(1, sum(1 for s in sentences if s.strip()))
    clarity_score = max(0, min(1, 1 - (avg_len - 20) / 60))

    action_verbs = ['led','developed','implemented','created','improved','increased','decreased','optimized','designed','launched','managed']
    action_count = sum(1 for v in action_verbs if re.search(r'\\b' + v + r'\\b', text, re.I))
    impact_score = min(1.0, action_count / 5.0)


    keyword_score = min(1.0, len(skills) / 8.0)

  
    total = (0.25 * clarity_score + 0.25 * impact_score + 0.25 * keyword_score + 0.25 * completeness) * 10
    details = {
        'sections': sections,
        'avg_sentence_length': avg_len,
        'action_count': action_count,
        'skill_count': len(skills)
    }
    return round(total, 2), details

def compare_with_job_title(resume_text, job_title):
    JOB_SKILLS = {
        'software engineer': ['python','javascript','git','docker','react','sql'],
        'data scientist': ['python','sql','pandas','numpy','machine learning','tensorflow'],
        'product manager': ['roadmapping','stakeholder','user research','analytics','sql']
    }
    key = job_title.strip().lower()
    expected = JOB_SKILLS.get(key, [])
    resume_skills = extract_skills_from_text(resume_text)
    matches = [s for s in resume_skills if s.lower() in expected]
    gaps = [s for s in expected if s not in resume_skills]
    return matches, gaps
