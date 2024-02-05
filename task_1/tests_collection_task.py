import pytest

from task_1.collection_task import unique_name_mentors, top_3_mentors, super_name_mentors
from task_1.data_mentors import mentors


def test_unique_name_mentors():
    actual = unique_name_mentors(mentors)
    expected = ('Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон,'
                ' Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, '
               'Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий')
    assert actual == expected


def test_top_3_mentors():
    actual = top_3_mentors(mentors)
    expected = 'Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
    assert actual == expected


def test_super_name_mentors():
    actual = super_name_mentors(mentors)
    expected = ' На курсах "Python-разработчик с нуля" и "Java-разработчик с нуля" преподают:Антон,Евгений,Максим\n'\
               ' На курсах "Python-разработчик с нуля" и "Fullstack-разработчик на Python" преподают:Александр,'\
               'Евгений,Елена,Кирилл,Максим,Олег,Роман\n'\
               ' На курсах "Python-разработчик с нуля" и "Frontend-разработчик с нуля" преподают:Александр,Евгений\n' \
               ' На курсах "Java-разработчик с нуля" и "Fullstack-разработчик на Python" преподают:Денис,Евгений,'\
               'Максим\n'
    assert actual == expected