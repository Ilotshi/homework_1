from flask import Flask
from utils import *

app = Flask(__name__)

@app.route("/")
def main_page():
    """Главная вьюха"""
    candidates = load_candidates()
    result = '<pre>'
    for candidate in candidates:
        result += f"""
        Имя кандидата - {candidate['name']}\n
        Позиция кандидата - {candidate['position']}\n
        {candidate['skills']}\n
        """
    result += '</pre>'
    return result

@app.route("/candidates/<int:uid>")
def page_candidate(uid):
    """Вьюха '/candidates/'"""
    candidate = get_by_pk(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += '<pre>'
    result += f"""
            Имя кандидата - {candidate['name']}\n
            Позиция кандидата - {candidate['position']}\n
            {candidate['skills']}\n
            """
    return result

@app.route("/skills/<skill>")
def page_skills(skill):
    """Вьюха '/skill/'"""
    result = '<pre>'
    valid_candidates = get_by_skill(skill)
    for valid_candidate in valid_candidates:
        result += f"""
        Имя кандидата - {valid_candidate['name']}\n
        Позиция кандидата - {valid_candidate['position']}\n
        {valid_candidate['skills']}\n"""
    result += '</pre>'
    return result
app.run()