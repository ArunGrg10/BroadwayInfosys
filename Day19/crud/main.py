from Day19.crud.create import create_student
from Day19.crud.read import read_student
from Day19.crud.update import update_student
from Day19.crud.delete import delete_student


def inquiry():
    selection = input("enter your choice c/r/u/d/e: ")
    selection = selection.lower()

    def exit_message():
        print("thank you! see you again.")


    if selection == "c":
        repeat = create_student()
        inquiry() if repeat else exit_message()

    elif selection == "r":
        student_id = input("enter the student id: ")

        repeat = read_student(student_id)
        inquiry() if repeat else exit_message()

    elif selection == "u":
        student_id = input("enter the student id: ")
        update_student(student_id)


    elif selection == "d":
        student_id = input("enter the student id: ")
        repeat = delete_student(student_id)
        inquiry() if repeat else exit_message()

    else:
        exit_message()





if __name__ == "__main__":
    inquiry()
