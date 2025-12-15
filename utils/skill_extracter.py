def extract_skills(text):
    with open("data/skills.txt", "r") as file:
        skills = [skill.strip() for skill in file.readlines()]

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
