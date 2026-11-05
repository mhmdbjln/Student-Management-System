class person:
    '''Enter personal information'''

    def __init__(self, name, ID, study_group):
        self.name = name
        self.ID = ID
        self.study_group = study_group


class student(person):
    def __init__(self, average, entering_year, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.average = average
        self.entering_year = entering_year

    def __repr__(self):
        return (f"Student name: {self.name}\n" +
                f"Student ID: {self.ID}\n" +
                f"Study group: {self.study_group}\n" +
                f"Average: {self.average}\n" +
                f"Entering year: {self.entering_year}")

    def show_all_student(self):
        return (f"\tname: {self.name}\t\tID: {self.ID}\t\tstudy group: {self.study_group}\t\taverage: {self.average}\t\tentering year: {self.entering_year}")


class teacher(person):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return (f"Teacher name: {self.name}\n" +
                f"Teacher ID: {self.ID}\n" +
                f"Study group: {self.study_group}")

    def show_all_teacher(self):
        return (f"\tname: {self.name}\t\tID: {self.ID}\t\tstudy group: {self.study_group}")


class studygroup:
    def __init__(self, group, codegroup):
        self.group = group
        self.codegroup = codegroup


filename_student = 'filestudent.txt'
filename_teacher = 'fileteacher.txt'
filename_advisor = 'fileadvisor.txt'
filename_group = 'filegroup.txt'
filename_beststudent = 'filebeststudent.txt'


def add_student(student_name, student_ID, group, average, entering_year):
    new_student = student(name=student_name, ID=student_ID, study_group=group, average=average, entering_year=entering_year)
    data = ','.join([new_student.name,new_student.ID,new_student.study_group,new_student.average,new_student.entering_year])
    file = open(filename_student, 'a')
    file.write(data + '\n')
    file.close()


def add_teacher(teacher_name, teacher_ID, group):
    new_teacher = teacher(name=teacher_name, ID=teacher_ID, study_group=group)
    data = ','.join([new_teacher.name, new_teacher.ID, new_teacher.study_group])
    file = open(filename_teacher, 'a')
    file.write(data + '\n')
    file.close()


def add_studygroup(group, group_code):
    new_studygroup = studygroup(group=group, codegroup=group_code)
    data = ','.join([new_studygroup.group, new_studygroup.codegroup])
    file = open(filename_group, 'a')
    file.write(data + '\n')
    file.close()


def update_student(student_ID, name=None, group=None, average=None, entering_year=None):
    student_ID = str(student_ID)
    file = open(filename_student, 'r')
    data = file.readlines()
    result = []
    for line in data:
        student_info = line.split(',')

        if student_ID == student_info[1]:
            if group is not None:
                student_info[2] = group

            if average is not None:
                student_info[3] = average

            if entering_year is not None:
                student_info[4] = entering_year

        up_student = student(name=student_info[0], ID=student_info[1], study_group=student_info[2], average=student_info[3], entering_year=student_info[4])
        dat = ','.join([up_student.name, up_student.ID, up_student.study_group, up_student.average, up_student.entering_year])
        result.append(dat)
    file.close()

    file = open(filename_student, 'w')
    file.write(''.join(result))
    file.close()


def update_teacher(teacher_ID, group=None):
    teacher_ID = str(teacher_ID)
    file = open(filename_teacher, 'r')
    data = file.readlines()
    result = []
    for line in data:
        teacher_info = line.split(',')

        if teacher_ID == teacher_info[1]:
            teacher_info[2] = group + '\n'

        up_teacher = teacher(name=teacher_info[0], ID=teacher_info[1], study_group=teacher_info[2])
        dat = ','.join([up_teacher.name, up_teacher.ID, up_teacher.study_group])
        result.append(dat)
    file.close()

    file = open(filename_teacher, 'w')
    file.write(''.join(result))
    file.close()


def search_student(name=None, student_ID=None):
    file = open(filename_student, 'r')
    data = file.readlines()

    if name is not None:
        for line in data:
            student_info = line.split(',')
            if name == student_info[0]:
                is_student = student(name=student_info[0], ID=student_info[1], study_group=student_info[2], average=student_info[3], entering_year=student_info[4])
                print(is_student)

    elif student_ID is not None:
        for line in data:
            student_info = line.split(',')
            if student_ID == student_info[1]:
                is_student = student(name=student_info[0], ID=student_info[1], study_group=student_info[2], average=student_info[3], entering_year=student_info[4])
                print(is_student)
    file.close()


def search_teacher(name=None, teacher_ID=None):
    file = open(filename_teacher, 'r')
    data = file.readlines()

    if name is not None:
        for line in data:
            teacher_info = line.split(',')
            if name == teacher_info[0]:
                is_teacher = teacher(name=teacher_info[0], ID=teacher_info[1], study_group=teacher_info[2])
                print(is_teacher)

    elif teacher_ID is not None:
        for line in data:
            teacher_info = line.split(',')
            if teacher_ID == teacher_info[1]:
                is_teacher = teacher(name=teacher_info[0], ID=teacher_info[1], study_group=teacher_info[2])
                print(is_teacher)
    file.close()


def advisor_teacher(student_name, teacher_name):
    file = open(filename_teacher, 'r')
    data = file.readlines()
    result = []
    for line in data:
        teacher_info = line.split(',')
        if teacher_name == teacher_info[0]:
            dat = ','.join([student_name, teacher_name])
            result.append(dat)
    file.close()

    file = open(filename_advisor, 'a')
    file.write(''.join(result) + '\n')
    file.close()


def best_student(code_group):
    code_group = str(code_group)
    file = open(filename_group, 'r')
    data = file.readlines()
    result = []
    for line in data:
        group = line.split(',')
        x = str(group[1][:-1])
        if x == code_group:
            dat = ''.join([group[0]])
            result.append(dat)
    file.close()

    file = open(filename_student, 'r')
    data = file.readlines()
    student_list = list()

    for line in data:
        student = line.split(',')
        if result[0] == student[2]:
            student_list.append(student)
    file.close()

    for i in range(3):
        scores = [int(i[3]) for i in student_list]
        maxx = max(scores)
        index = scores.index(maxx)
        print(f"\tname: {student_list[index][0]}"+f"\t\tID: {student_list[index][1]}"+f"\t\tstudy group: {student_list[index][2]}"+f"\t\taverage: {student_list[index][3]}"+f"\t\tentering year: {student_list[index][4]}")
        student_list[index][3] = 0


def show_student():
    file = open(filename_student, 'r')
    data = file.readlines()

    for line in data:
        student_info = line.split(',')
        is_student = student(name=student_info[0], ID=student_info[1], study_group=student_info[2], average=student_info[3], entering_year=student_info[4])
        print(is_student.show_all_student())
    file.close()


def show_teacher():
    file = open(filename_teacher, 'r')
    data = file.readlines()

    for line in data:
        teacher_info = line.split(',')
        is_teacher = teacher(name=teacher_info[0], ID=teacher_info[1], study_group=teacher_info[2])
        print(is_teacher.show_all_teacher())
    file.close()


def show_menu():
    print('\t1. STUDENT\n'
          '\t2. TEACHER\n'
          '\t3. Advisor teacher for the student\n'
          '\t4. New study group\n'
          '\t5. Top student\n'
          '\t6. Exit')


def show_menu_student():
    print('\t1. Add student\n'
          '\t2. Update student\n'
          '\t3. Search student\n'
          '\t4. Show All student\n'
          '\t5. Main menu')


def show_menu_teacher():
    print('\t1. Add teacher\n'
          '\t2. Update teacher\n'
          '\t3. Search teacher\n'
          '\t4. Show All teacher\n'
          '\t5. Main menu')


print('WELCOME*_*')
while True:
    show_menu()
    user_input = input('Please enter an option: ')

    if user_input == '1':
        while True:
            show_menu_student()
            input1 = input('Please enter an option: ')

            if input1 == '1':
                student_name = input('Please enter name: ')
                ID = input('Please enter ID: ')
                group = input('Please enter study group: ')
                average = input('Please enter average: ')
                year = input('Please enter entering year: ')
                add_student(student_name, ID, group, average, year)
                print('Student added')

            elif input1 == '2':
                ID = input('Please enter ID: ')
                while True:
                    print('\t1. Update study group\n'
                          '\t2. Update average\n'
                          '\t3. Update entering year\n'
                          '\t4. Student menu')
                    update_input = input('Please enter your option: ')

                    if update_input == '1':
                        new_group = input('Please enter new study group: ')
                        update_student(ID, group=new_group)
                        print('Group updated')
                    elif update_input == '2':
                        new_average = input('Please enter new average: ')
                        update_student(ID, average=new_average)
                        print('Average updated')
                    elif update_input == '3':
                        new_year = input('Please enter new entering year: ')
                        update_student(ID, entering_year=new_year)
                        print('Entering year updated')
                    elif update_input == '4':
                        break
                    else:
                        print('ERROR: please enter correct number.')

            elif input1 == '3':
                x = input('1.Name or 2.Student number?: ')
                if x == '1':
                    isname = input('Please enter name: ')
                    search_student(name=isname)
                elif x == '2':
                    isID = input('Please enter Student number: ')
                    search_student(student_ID=isID)
                else:
                    print('ERROR: please enter correct number.')

            elif input1 == '4':
                show_student()
                print()
            elif input1 == '5':
                break
            else:
                print('ERROR: please enter correct number.')

    elif user_input == '2':
        while True:
            show_menu_teacher()
            input2 = input('Please enter an option: ')

            if input2 == '1':
                teacher_name = input('Please enter name: ')
                ID = input('Please enter ID: ')
                group = input('Please enter study group: ')
                add_teacher(teacher_name, ID, group)
                print('Teacher added')

            elif input2 == '2':
                ID = input('Please enter ID: ')
                new_group = input('Please enter new group: ')
                update_teacher(ID, group=new_group)
                print('Group updated')

            elif input2 == '3':
                x = input('1.Name or 2.Teacher number?: ')
                if x == '1':
                    isname = input('Please enter name: ')
                    search_teacher(name=isname)
                elif x == '2':
                    isID = input('Please enter Teacher number: ')
                    search_teacher(teacher_ID=isID)
                else:
                    print('ERROR: please enter correct number.')

            elif input2 == '4':
                show_teacher()
            elif input2 == '5':
                break
            else:
                print('ERROR: please enter correct number.')

    elif user_input == '3':
        name_student = input('please enter student name: ')
        name_teacher = input('please enter teacher name: ')
        advisor_teacher(name_student, name_teacher)

    elif user_input == '4':
        new_studygroup = input('Please enter name study group: ')
        new_code = input('Please enter group code: ')
        add_studygroup(new_studygroup, new_code)
        print('Code and study group were added')

    elif user_input == '5':
        code = input('please enter code group: ')
        best_student(code)

    elif user_input == '6':
        break
    else:
        print('ERROR: please enter correct number.')
