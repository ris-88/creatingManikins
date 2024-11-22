import file_operations
from faker import Faker
import random

fake = Faker("ru_RU")
SKILLS = ["Стремительный прыжок", "Электрический выстрел", "Ледяной удар", "Стремительный удар",
          "Кислотный взгляд", "Тайный побег", "Ледяной выстрел", "Огненный заряд"]

ALPHABET = {
    'а': 'а͠', 'б': 'б̋', 'в': 'в͒͠',
    'г': 'г͒͠', 'д': 'д̋', 'е': 'е͠',
    'ё': 'ё͒͠', 'ж': 'ж͒', 'з': 'з̋̋͠',
    'и': 'и', 'й': 'й͒͠', 'к': 'к̋̋',
    'л': 'л̋͠', 'м': 'м͒͠', 'н': 'н͒',
    'о': 'о̋', 'п': 'п̋͠', 'р': 'р̋͠',
    'с': 'с͒', 'т': 'т͒', 'у': 'у͒͠',
    'ф': 'ф̋̋͠', 'х': 'х͒͠', 'ц': 'ц̋',
    'ч': 'ч̋͠', 'ш': 'ш͒͠', 'щ': 'щ̋',
    'ъ': 'ъ̋͠', 'ы': 'ы̋͠', 'ь': 'ь̋',
    'э': 'э͒͠͠', 'ю': 'ю̋͠', 'я': 'я̋',
    'А': 'А͠', 'Б': 'Б̋', 'В': 'В͒͠',
    'Г': 'Г͒͠', 'Д': 'Д̋', 'Е': 'Е',
    'Ё': 'Ё͒͠', 'Ж': 'Ж͒', 'З': 'З̋̋͠',
    'И': 'И', 'Й': 'Й͒͠', 'К': 'К̋̋',
    'Л': 'Л̋͠', 'М': 'М͒͠', 'Н': 'Н͒',
    'О': 'О̋', 'П': 'П̋͠', 'Р': 'Р̋͠',
    'С': 'С͒', 'Т': 'Т͒', 'У': 'У͒͠',
    'Ф': 'Ф̋̋͠', 'Х': 'Х͒͠', 'Ц': 'Ц̋',
    'Ч': 'Ч̋͠', 'Ш': 'Ш͒͠', 'Щ': 'Щ̋',
    'Ъ': 'Ъ̋͠', 'Ы': 'Ы̋͠', 'Ь': 'Ь̋',
    'Э': 'Э͒͠͠', 'Ю': 'Ю̋͠', 'Я': 'Я̋',
    ' ': ' '
}


def generate_character():
    new_skills = []
    new_skill = ""
    random_skills = random.sample(SKILLS, 3)

    for skill in random_skills:
        new_skill = ""
        for letter in skill:
            for new_letter in ALPHABET:
                if letter == new_letter:
                    new_skill += ALPHABET[new_letter]
        new_skills.append(new_skill)

    context = {
        "first_name": fake.first_name_male(),
        "last_name": fake.last_name_male(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": random.randrange(3, 18),
        "agility": random.randrange(3, 18),
        "endurance": random.randrange(3, 18),
        "intelligence": random.randrange(3, 18),
        "luck": random.randrange(3, 18),
        "skill_1": new_skills[0],
        "skill_2": new_skills[1],
        "skill_3": new_skills[2]
    }
    return context


if __name__ == '__main__':
    context = generate_character()
    result = context["first_name"] + context["last_name"]
    file_operations.render_template("src/charsheet.svg", f"src/output/svg/{result}.svg", context)
