# На входе всех тестов будет одинаковый курс

import pytest

from program import courses_list


@pytest.mark.parametrize("course_index, expected_output", [
    (0, "На курсе Java-разработчик с нуля есть тёзки: Алексей Степанов, Антон Глушков, Иван Бочаров"),
    (1, "На курсе Fullstack-разработчик на Python есть тёзки: Александр Бардин, Денис Ежков, Кирилл Табельский, Олег Булыгин"),
    (2, "На курсе Python-разработчик с нуля есть тёзки: Алена Батицкая, Александр Ульянцев, Евгений Шмаргунов, Максим Филипенко, Роман Гордиенко"),
    (3, "На курсе Frontend-разработчик с нуля есть тёзки: Алена Батицкая, Александр Шлейко, Александр Фитискин, Денис Ежков, Владимир Чебукин, Евгений Шек")
])
def test_same_names(course_index, expected_output, capsys):
    unique_names = set()
    mentors_name = [name.split()[0] for name in courses_list[course_index]['mentors']]
    unique_names = sorted(set(mentors_name))

    same_name_list = []
    for name in unique_names:
        if mentors_name.count(name) > 1:
            for full_names in courses_list[course_index]['mentors']:
                if name in full_names.split()[0]:
                    same_name_list.append(full_names)
                    same_name_list = sorted(same_name_list)
    if same_name_list:
        print(f'На курсе {courses_list[course_index]["title"]} есть тёзки: {", ".join(same_name_list)}')

    captured = capsys.readouterr()
    assert captured.out.strip() == expected_output.strip()
