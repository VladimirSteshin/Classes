class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'error'

    def __str__(self):
        for i in self.grades.values():
            print(f'{self.name}\n{self.surname}\nСредняя оценка за домашние задания: {str(round(sum(i) / len(i), 1))}')
            print('Курсы в процессе: ', end='')
            print(*self.courses_in_progress, sep=', ')
            print('Оконченные курсы: ', end='')
            print(*self.finished_courses, sep=', ')
            return ''

    def compare(self, another_student):
        if isinstance(another_student, Student):
            res_self = 0
            for i in self.grades.values():
                res_self = round(sum(i) / len(i), 1)
            res_another = 0
            for i in another_student.grades.values():
                res_another = round(sum(i) / len(i), 1)
            if res_self < res_another:
                return f'{another_student.name} {another_student.surname} is the best student!'
            elif res_self > res_another:
                return f'{self.name} {self.surname} is the best student!'
            else:
                return f'Students are equal.'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        for i in self.grades.values():
            return f'{self.name}\n{self.surname}\nСредняя оценка за лекции: {str(round(sum(i) / len(i), 1))}'

    def compare(self, another_lecturer):
        if isinstance(another_lecturer, Lecturer):
            res_self = 0
            for i in self.grades.values():
                res_self = round(sum(i) / len(i), 1)
            res_another = 0
            for i in another_lecturer.grades.values():
                res_another = round(sum(i) / len(i), 1)
            if res_self < res_another:
                return f'{another_lecturer.name} {another_lecturer.surname} is the best lecturer!'
            elif res_self > res_another:
                return f'{self.name} {self.surname} is the best lecturer!'
            else:
                return f'Lecturers are equal.'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'{self.name}\n{self.surname}'


best_student = Student('Ruoy', 'Eman', 'Male')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

good_student = Student('Bellatrix', 'Le Strange', 'Female')
good_student.courses_in_progress += ['Python']
good_student.courses_in_progress += ['Git']
good_student.finished_courses += ['Введение в программирование']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_reviewer = Reviewer('Dolores', 'Umbridge')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 7)
cool_reviewer.rate_hw(good_student, 'Python', 9)
cool_reviewer.rate_hw(good_student, 'Python', 8)
cool_reviewer.rate_hw(good_student, 'Python', 9)

good_reviewer = Reviewer('Cornelius', 'Fudge')
good_reviewer.courses_attached += ['Git']
good_reviewer.rate_hw(best_student, 'Git', 10)
good_reviewer.rate_hw(best_student, 'Git', 9)
good_reviewer.rate_hw(best_student, 'Git', 8)
good_reviewer.rate_hw(good_student, 'Git', 7)
good_reviewer.rate_hw(good_student, 'Git', 5)
good_reviewer.rate_hw(good_student, 'Git', 7)

cool_lecturer = Lecturer('Severus', 'Snape')
cool_lecturer.courses_attached += ['Python']

good_lecturer = Lecturer('Rubeus', 'Hagrid')
good_lecturer.courses_attached += ['Git']

best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer, 'Python', 8)
best_student.rate_hw(cool_lecturer, 'Python', 7)

best_student.rate_hw(good_lecturer, 'Git', 6)
best_student.rate_hw(good_lecturer, 'Git', 8)
best_student.rate_hw(good_lecturer, 'Git', 7)

print(cool_lecturer.compare(good_lecturer))
print(best_student.compare(good_student))


def summ_student_grades(students, course):
    summ = 0
    for name in students:
        if isinstance(name, Student) and course in name.courses_in_progress:
            for mark in name.grades[course]:
                summ += mark
    return f'Общее количество баллов студентов на курсе {course}: {summ}'


def summ_lector_grades(lectors, course):
    summ = 0
    for name in lectors:
        if isinstance(name, Lecturer) and course in name.courses_attached:
            for mark in name.grades[course]:
                summ += mark
    return f'Общее количество баллов лекторов на курсе {course}: {summ}'
