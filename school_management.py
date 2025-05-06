# Project Title: School Management System
# Author: Sebastian Hsiao
# Date: 2025-04-22

"""
This script simulates a simple school management system
using classes to represent students, teachers, and courses.
It includes functionality to assign grades, manage friendships,
and display a summary of the school environment.
"""

# Importing necessary libraries
import random

# Base class for all people in the school
class Person:
    def __init__(self, name):
        self.name = name  # Stores the name of the person

# Student class inherits from Person
class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        self.grades = {}  # Dictionary to store course name -> grade
        self.favorite_subject = None  # Will hold the subject with the highest grade
        self.friends = set()  # Set of friends' names

    def add_friend(self, other_student):
        # Adds a student as a friend and ensures mutual friendship
        self.friends.add(other_student.name)
        other_student.friends.add(self.name)

    def assign_grade(self, course, grade):
        # Assigns a grade for a specific course
        self.grades[course.name] = grade
        self.update_favorite_subject()  # Updates favorite subject after assigning grade

    def update_favorite_subject(self):
        # Updates the favorite subject based on the highest grade
        if self.grades:
            self.favorite_subject = max(self.grades, key=self.grades.get)

# Teacher class inherits from Person
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.courses = []  # List of courses the teacher teaches

    def assign_course(self, course):
        # Assigns a course to the teacher
        self.courses.append(course)
        course.teacher = self

# Represents a school course
class Course:
    def __init__(self, name):
        self.name = name  # Course name
        self.teacher = None  # Assigned teacher
        self.students = []  # List of enrolled students

    def enroll_student(self, student):
        # Adds a student to the course
        self.students.append(student)

# Main school class that holds all people and courses
class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        # Adds a student to the school
        self.students.append(student)

    def add_teacher(self, teacher):
        # Adds a teacher to the school
        self.teachers.append(teacher)

    def add_course(self, course):
        # Adds a course to the school
        self.courses.append(course)

    def simulate_grades(self):
        # Randomly assigns grades to students for each course they are in
        for course in self.courses:
            for student in course.students:
                grade = random.randint(60, 100)  # Random grade between 60 and 100
                student.assign_grade(course, grade)

    def simulate_friendships(self):
        # Randomly establishes friendships among students
        for student in self.students:
            potential_friends = [s for s in self.students if s != student]
            friends = random.sample(potential_friends, k=min(2, len(potential_friends)))
            for f in friends:
                student.add_friend(f)

    def summary(self):
        # Prints a summary of each student's status
        print("Welcome to {} High School Simulator!\n".format(self.name))
        for student in self.students:
            print("Student: {}".format(student.name))
            print("  Grades: {}".format(student.grades))
            print("  Favorite Subject: {}".format(student.favorite_subject))
            print("  Friends: {}\n".format(", ".join(student.friends)))
