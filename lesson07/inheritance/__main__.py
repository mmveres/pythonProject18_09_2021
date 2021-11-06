from lesson07.inheritance.doctor import Doctor
from lesson07.inheritance.fighter import Fighter
from lesson07.inheritance.student import Student

if __name__ == '__main__':
    st1 = Student("Tom",20,1,75)
    doc1 = Doctor("Haus", 60, 666, 65)
    fighter1 = Fighter("Conan", 30, 100,90,100)

    people = [st1, doc1, fighter1]


    for human in people:
        print(human)
        if isinstance(human, Student):
            print(human.group)

    max_age_human = people[0]
    for human in people:
        if max_age_human.age< human.age:
            max_age_human = human
    print(max_age_human)