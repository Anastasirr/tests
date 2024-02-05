from data_mentors import *


def unique_name_mentors(mentors):
    all_list = []
    for mentor_ in mentors:
        if mentor_ in mentors:
            all_list.extend(mentor_)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)

    unique_names = set(all_names_list)

    all_names_sorted = sorted(unique_names)
    return f'Уникальные имена преподавателей: {", ".join(all_names_sorted)}'


def top_3_mentors(mentors):
    all_list = []
    for mentor_ in mentors:
        if mentor_ in mentors:
            all_list.extend(mentor_)
    all_names_list = []
    for mentor in all_list:
        name = mentor.split()[0]
        all_names_list.append(name)
    unique_names = set(all_names_list)

    popular = []
    for name in unique_names:
        popular.append((name, all_names_list.count(name)))
    popular = list(set(popular))
    popular.sort(key=lambda x: x[1], reverse=True)
    top_3 = popular[0:3]

    top__ = []
    for top_3_f in top_3:
        top__.append(f'{top_3_f[0]}: {top_3_f[1]} раз(а)')
    return ", ".join(top__)


def super_name_mentors(mentors):
    mentors_names = []
    for mentor_ in mentors:
        course_names = []
        for name in mentor_:
         course_names.append(name.split()[0])
        mentors_names.append(course_names)

    pairs = []
    list_of_mentors = []

    for id1 in range(len(mentors_names)):
        for id2 in range(len(mentors_names)):
            if id1 == id2: continue
            intersection_set = set(mentors_names[id1]) & set(mentors_names[id2])
            if len(intersection_set) > 0:
                pair = {courses[id1], courses[id2]}
                if pair not in pairs:
                    pairs.append(pair)
                    all_names_sorted = sorted(intersection_set)
                    list_of_mentors.append(f' На курсах "{courses[id1]}" и "{courses[id2]}" преподают:{",".join(all_names_sorted)}\n')
    return f"{list_of_mentors[0]}{list_of_mentors[1]}{list_of_mentors[2]}{list_of_mentors[3]}"
