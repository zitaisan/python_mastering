students = []
n_students = []
sort = False
def addStudents():

    global students
    print("Введите студентов в формате ('Имя', оценка). Введите 'stop' для завершения.")
    comm = ''
    while True:
        comm = input('Введите студента: ')
        if comm == 'stop':
            break
        else:
            try:
                student = eval(comm)
                if isinstance(student, tuple) and len(student) == 2:
                    students.append(student)
                else:
                    print("Ошибка форматa ('Имя', оценка).")
            except Exception as e:
                print(f'Ошибка: {e}')
def sortStudents(students, choice):
    global sort
    sort = True
    return sorted(students, key=lambda student: student[1], reverse=choice)
def showStudents(students):
    for i in students:
        print(i)
def main():
    global sort, students, n_students
    comm=''
    while comm!='exit':
        comm = input('Выберите команду: add, sort, show, exit ')
        try:
            if comm == 'add':
                addStudents()
            elif comm == 'sort':
                rev = input('возрастание или убывание: ')
                if rev == 'возрастание':
                    n_students = sortStudents(students, False)
                    print('Отсортировалось по возрастанию')
                elif rev == 'убывание':
                    n_students = sortStudents(students, True)
                    print('Отсортировалось по убыванию')
                else:
                    print('Попробуйте еще раз')
            elif comm == 'show':
                showStudents(students)
                if sort == True:
                    print('после сортировки')
                    showStudents(n_students)
            elif comm == 'exit':
                exit()
            else:
                print('Попробуйте еще раз')
        except Exception as e:
            print(f'Ошибка: {e}')
main()



