class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_score = 0
        students_list.append(self.__dict__)

    def rate_lecture(self, lektor, course, grade):
        if isinstance(lektor, Lecturer) and course in self.courses_in_progress and course in lektor.courses_attached:
            lektor.grades += [grade]
            lektor.average_score = round(sum(lektor.grades) / len(lektor.grades), 2)


    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.average_score < other.average_score

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за домашние задания: {self.average_score} \n' \
               f'Курсы в процессе изучения: {self.courses_in_progress} \n' \
               f'Завершенные курсы: {self.finished_courses}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        self.grades = []
        self.average_score = 0
        super().__init__(name, surname)
        lektors_list.append(self.__dict__)

    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname} \n' \
               f'Средняя оценка за лекции: {self.average_score}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.average_score < other.average_score

class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.courses_attached = []
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            sum_hw = 0
            counter = 0
            for key, value in student.grades.items():
                sum_hw += sum(value) / len(value)
                counter += 1
            student.average_score = round(sum_hw / counter, 2)


    def __str__(self):
        return f'Имя: {self.name} \n' \
               f'Фамилия: {self.surname}'

students_list = []
lektors_list = []

def average_grade_hw(students, courses):
    sum_gh = 0
    counter = 0
    for student in students:
        for key, value in student['grades'].items():
            if courses in key:
                sum_gh += sum(value) / len(value)
                counter += 1
    return round(sum_gh / counter, 2)



def average_grade_lecture(lecturers, courses):
    sum_gl = 0
    counter = 0
    for lector in lecturers:
        if courses in lector["courses_attached"]:
           sum_gl += sum(lector["grades"]) / len(lector["grades"])
           counter += 1
    return round(sum_gl / counter, 2)



ivanov = Student('Иван', 'Иванов', 'м')
ivanov.courses_in_progress += ['Python']
ivanov.courses_in_progress += ['Git']
ivanov.finished_courses += ['Введение в программирование']

petrov = Student('Петр', 'Петров', 'м')
petrov.courses_in_progress += ['Python']
petrov.courses_in_progress += ['Git']
petrov.finished_courses += ['Введение в программирование']

smirnov = Lecturer('Григорий', 'Смирнов')
smirnov.courses_attached += ['Python']

sidorov = Lecturer('Алекс', 'Сидоров')
sidorov.courses_attached += ['Git']

utkin = Reviewer('Андрей', 'Уткин')
utkin.courses_attached += ['Git']

lisin = Reviewer('Олег', 'Лисин')
lisin.courses_attached += ['Python']


utkin.rate_hw(ivanov, 'Git', 7)
utkin.rate_hw(ivanov, 'Git', 8)
utkin.rate_hw(ivanov, 'Git', 7)
utkin.rate_hw(petrov, 'Git', 10)

lisin.rate_hw(ivanov, 'Python', 6)
lisin.rate_hw(ivanov, 'Python', 8)
lisin.rate_hw(ivanov, 'Python', 8)
lisin.rate_hw(petrov, 'Python', 6)
lisin.rate_hw(petrov, 'Python', 4)
lisin.rate_hw(petrov, 'Python', 6)

ivanov.rate_lecture(smirnov, 'Python', 7)
ivanov.rate_lecture(smirnov, 'Python', 8)
ivanov.rate_lecture(smirnov, 'Python', 5)
petrov.rate_lecture(smirnov, 'Python', 8)
petrov.rate_lecture(smirnov, 'Python', 8)
petrov.rate_lecture(smirnov, 'Python', 8)

ivanov.rate_lecture(sidorov, 'Git', 9)
ivanov.rate_lecture(sidorov, 'Git', 7)
ivanov.rate_lecture(sidorov, 'Git', 6)
petrov.rate_lecture(sidorov, 'Git', 8)

print()
print(ivanov)
print()
print(petrov)
print()
print(sidorov)
print()
print(smirnov)
print()
print(utkin)
print()
print(lisin)
print()
#print(students_list)
print("Средняя оценка за домашние задания:" , average_grade_hw(students_list , 'Git'))
print("Средняя оценка за лекции:" , average_grade_lecture(lektors_list , 'Python'))

#print(ivanov.__dict__)
print(smirnov > sidorov)
print()
print(ivanov > petrov)
