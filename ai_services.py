import os

def generate_summaries(highlights):
    if not highlights:
        return ["Experienced professional with proven track record."]
    return [
        f"{highlights} — results-driven professional with strong technical background.",
        f"{highlights} — experienced in delivering measurable impact and cross-functional collaboration.",
        f"{highlights} — focused on scalable solutions and data-driven decision making."
    ]

def rewrite_sentence_suggestions(sentence):
    if not sentence:
        return []
    s = sentence.strip()
    return [
        s.replace('responsible for', 'led').replace('Was', 'Led'),
        s + ' Achieved measurable impact by focusing on outcome and metrics.'
    ]

def ats_preview(resume_text):
    lines = []
    for line in resume_text.splitlines():
        clean = ' '.join(line.strip().split())
        if clean:
            lines.append(clean)
    return '\n'.join(lines)
