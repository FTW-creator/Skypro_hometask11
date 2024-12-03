from flask import Flask, render_template
from functions import load_candidates, get_by_skill, get_by_name, get_by_id

app = Flask(__name__)


@app.route("/")
def index():
    candidates = load_candidates()
    return render_template('list.html', candidates = candidates)


@app.route("/candidates/<int:x>")
def candidate_page(x):
    candidate = get_by_id(x)
    return render_template('card.html', candidate = candidate)

@app.route("/search/<candidate_name>")
def candidates_search(candidate_name):
    candidates, amount = get_by_name(candidate_name)
    return render_template('search.html', candidates = candidates, amount = amount)



@app.route("/skills/<skill>")
def skill_search(skill):
    candidates, amount = get_by_skill(skill)
    return render_template('skill.html', candidates = candidates, amount = amount, skill = skill)


if __name__ == "__main__":
    app.run()
