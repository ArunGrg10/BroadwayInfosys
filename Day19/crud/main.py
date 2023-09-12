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
        create_student()

    elif selection == "r":
        read_student()

    elif selection == "u":
        update_student()

    elif selection == "d":
        delete_student()
    else:
        exit_message()





if __name__ == "__main__":
    inquiry()
