# AUTHOR:
# This template is write by:
# LE Nhu Chu Hiep <hieplnc.m20ict@st.usth.edu.vn>
#
# LICENSE:
# These lines need to be copied together with code
# when it is used by others.
#

# Import section
# TODO: import proper module for running script
import curses

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

# Example of course_credits as key-value (course_obj: credit_value):
course_credits = {
    course_math: 4,
    course_language: 4,
    course_philosophy: 1,
}
"""
students = []
courses = []

# TODO: write down your course and its credit.
course_credits = {}


# Auxiliary class
class Window:
    def __init__(self, win, h, w, start_h, start_w):
        self.children = {}
        self.win = win
        self.h = h
        self.w = w
        self.sh = start_h
        self.sw = start_w
        self.text = ""

    def spawn(self):
        nwin = curses.newwin(self.h, self.w, self.sh, self.sw)
        return Window(nwin, self.h, self.w, self.sh, self.sw)

    def add_sub(self, name: str, sub):
        self.children[name] = sub

    def refresh(self):
        self.win.refresh()
        for sub in self.children.values():
            sub.refresh()


class Terminal:
    """simple curses object"""

    def __init__(self):
        self.key = -1
        self.screen = self.screen_init()
        self.screen.add_sub("intro", self.intro_init())

    def __del__(self):
        curses.endwin()

    def screen_init(self):
        screen = Window(curses.initscr(), int(curses.LINES), int(curses.COLS), 0, 0)
        # screen.win.keypad(True) # THIS IS ILLEGAL
        curses.noecho()
        curses.cbreak()
        # curses.curs_set(0)
        return screen

    def intro_init(self) -> Window:
        intro_box = self.screen.spawn()
        intro_box.h = int(intro_box.h / 3)
        intro_box.w = int(intro_box.w / 2)
        intro_box = intro_box.spawn()
        intro_box.win.box()

        intro = intro_box.spawn()
        intro_w_base = intro.w
        intro.h -= 2
        intro.w -= 2 + int(intro_w_base / 5)
        intro.sw += int(intro_w_base / 8)
        intro.sh += 1
        intro = intro.spawn()

        # TODO: [fix this but I don't care]
        # If window font size is too big,
        # this text will cause errors
        intro_str = """
The program is written by author LE Nhu Chu Hiep.
This is default simple curses program to demo the
method which could be used to design terminal base
software.
        """
        intro.win.addstr(intro_str)

        intro_box.add_sub("noused_intro", intro)
        return intro_box

    def draw(self, *args, **kwargs):
        pass

    def update(self, key):
        pass

    def refresh(self):
        self.key = self.screen.win.getch()
        self.update(self.key)
        self.screen.refresh()

    def run(self):
        self.draw()
        self.screen.refresh()
        while self.key != 4:
            self.refresh()


class EduObj:
    """education object"""

    def getname(self):
        return self.__class__.__name__

    def input(self, *args, **kwargs):
        print(f"(Default list function of {self.__class__.__name__} object)")

    def info(self, *args, **kwargs):
        print(f"(Default info function of {self.__class__.__name__} object)")


# Class section
class StudentScreen(Terminal):
    def __init__(self):
        super().__init__()
        self.quest_count = 1

    def create_quest(self, quest_sister, quest_str, quest_id):
        q0 = quest_sister.spawn()
        q0.sh += q0.h
        q0.h = 4
        q0 = q0.spawn()

        # design question inside question box
        q0_quest = q0.spawn()
        q0_quest.h = 1
        q0_quest = q0_quest.spawn()
        q0_quest.win.addstr(quest_str)
        q0.add_sub("quest", q0_quest)

        q0_ans = q0_quest.spawn()
        q0_ans.sh += q0_ans.h
        q0_ans.h = 3
        q0_ans = q0_ans.spawn()
        q0_ans.win.box()
        q0.add_sub("ans", q0_ans)

        self.screen.add_sub(quest_id, q0)
        return q0

    # TODO: complete implementation for whole student information draw
    def draw(self, *args, **kwargs):
        quest_oldest = self.screen.children["intro"].spawn()
        q1 = self.create_quest(quest_oldest, "Q1. [default] Student name:", "q1")
        q2 = self.create_quest(q1, "Q2. [default] Student id:", "q2")

    # TODO: complete implementation for interface interaction
    def update(self, key):
        quest = self.screen.children[f"q{self.quest_count}"].children["ans"]
        if key == ord("\n"):
            self.quest_count = self.quest_count % 2 + 1
        else:
            if key == 263:
                if len(quest.text) > 0:
                    quest.win.clear()
                    quest.win.box()
                    quest.text = quest.text[:-1]
            else:
                quest.text += chr(key)
            quest.win.addstr(1, 1, quest.text)


# TODO: complete implementation of this class.
class Student(EduObj):
    """student information"""

    def __init__(self):
        self.my_gpa = None

    def get_gpa(self):
        return self.my_gpa

    # TODO: calculate this student GPA with numpy array.
    def cal_gpa(self, courses: list):
        clsn = self.__class__.__name__
        print(f"(Default cal_gpa function of {clsn} object)")

    # TODO: fancy print of my GPA.
    def info_gpa(self):
        clsn = self.__class__.__name__
        print(f"(Default info_gpa function of {clsn} object)")


# TODO: complete implementation of this class.
class Course(EduObj):
    """course information"""

    def __init__(self):
        pass

    # TODO: inform student round-down marks with math floor().
    def info_round_marks(self):
        clsn = self.__class__.__name__
        print(f"(Default round mark function of {clsn} object)")


# Auxiliary function section
def list_info(list_obj):
    # NOTE: implement your fancy list display here.
    for idx, obj in enumerate(list_obj):
        print(f"--- {obj.getname().lower()} {idx} ---")
        if isinstance(obj, EduObj):
            obj.info()
        if isinstance(obj, Course):
            obj.info_round_marks()
        if isinstance(obj, Student):
            if obj.get_gpa() is None:
                obj.cal_gpa(courses)
            obj.info_gpa()


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

    opt = int(
        input(
            """
            Choose your option:
0. Quit test.
1. Show simple curses implementation.
2. Test with normal terminal.

Your option is:"""
        )
    )

    if opt == 0:
        exit(0)

    if opt == 2:
        print("###### input ######")
        input_func()

        print("\n###### list ######")
        list_func()

    else:
        print("\n###### windows ######")
        terminal = StudentScreen()
        terminal.run()
