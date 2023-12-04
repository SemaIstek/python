class student():
    school_name='AYC'
    number_of_student =0
    student_list=[]
    def __init__(self, name, surname, age, grades):
        self.name=name
        self.surname=surname
        self.age=age
        self.grades=grades
        self.mail=(self.name[0]+'.'+self.surname+'@infotech.eu').lower()
        student.number_of_student +=1
        student.student_list.append([self.name,self.surname,self.mail])
    def avarage(self):
        return sum(self.grades) / len(self.grades)
    def intro(self):
        return f'{self.name}   {self.surname} ogrencisinin okul adi: {self.school_name} '
    
        

student_1=student('ali','veli',15,[40,50,60,70])
student_2=student('eslem','selin',16,[70,80,90,98])
print(student_1.avarage())
print(student_1.mail)
student_1.name='Omer'
print(student_1.mail)
print(student_1.school_name)
print(student.school_name)
print(student_1.intro())
student_1.school_name='TED'
print(student.school_name)
print(student.number_of_student)
print(student.student_list)
student.student_list[0][0]='alper'
for i in student.student_list:
    print(i)
for i in student.student_list:
    print(i[2])

print(student_1.__dict__)
student_dict=student_1.__dict__
print(student_dict['name'])
