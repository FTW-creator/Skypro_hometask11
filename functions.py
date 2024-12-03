import json


def load_candidates(filename="candidates.json"):
    with open(filename, 'r', encoding='utf-8') as file:
        candidates = json.loads(file.read())
        return candidates


def get_by_id(id):
    return load_candidates()[id - 1]


def get_by_name(name):
    appropriate_candidates = []
    for candidate in load_candidates():
        if name.lower() in candidate['name'].lower().split(" "):
            appropriate_candidates.append(candidate)
    return appropriate_candidates, len(appropriate_candidates)


def get_by_skill(skill_name):
    appropriate_candidates = []
    for candidate in load_candidates():
        if skill_name.lower() in candidate['skills'].lower().split(", "):
            appropriate_candidates.append(candidate)
    return appropriate_candidates, len(appropriate_candidates)
