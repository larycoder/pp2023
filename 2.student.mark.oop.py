# AUTHOR:
# This template is write by:
# LE Nhu Chu Hiep <hieplnc.m20ict@st.usth.edu.vn>
#
# LICENSE:
# These lines need to be copied together with code
# when it is used by others.
#

# Hint section
"""
1. Student hold his/her own information.
2. Course hold its own information and student list belong to it.
3. For each student in a course, he/she is assigned corresponding mark.
"""

# DATA section
"""
students = [student_obj_1, student_obj_2, ...]
courses = [courses_obj_1, courses_obj_2, ...]
"""
students = []
courses = []


# Class section
class EduObj:
    """education object"""

    def getname(self):
        return self.__class__.__name__

    def input(self, *args, **kwargs):
        print(f"(Default list function of {self.__class__.__name__} object)")

    def info(self, *args, **kwargs):
        print(f"(Default info function of {self.__class__.__name__} object)")


# TODO: complete implementation of this class.
class Student(EduObj):
    """student information"""

    def __init__(self):
        pass


# TODO: complete implementation of this class.
class Course(EduObj):
    """course information"""

    def __init__(self):
        pass


# Auxiliary function section
def list_info(list_obj):
    # NOTE: implement your fancy list display here.
    for idx, obj in enumerate(list_obj):
        print(f"--- {obj.getname().lower()} {idx} ---")
        if isinstance(obj, EduObj):
            obj.info()


# Test function section
def input_func():
    nb = int(input("Number of student: "))
    for i in range(nb):
        student = Student()
        student.input()
        students.append(student)

    nb = int(input("Number of course: "))
    for i in range(nb):
        course = Course()
        course.input()
        courses.append(course)


def list_func():
    print("--------- Student information ---------")
    list_info(students)
    print("------------------\n")

    print("--------- Course information ---------")
    list_info(courses)
    print("------------------\n")


# Test section
if __name__ == "__main__":
    print("Hello world")
    print("Testing program:\n")

    print("###### input ######")
    input_func()

    print("\n###### list ######")
    list_func()
