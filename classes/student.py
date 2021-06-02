import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/students.csv")

class Student:
    def __init__(self, name, age, role, school_id, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role
        self.school_id = school_id
    
    @classmethod
    def all_students(cls):
        student_list = []
        with open(path) as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for line in dict_reader:
                student_list.append(cls(**line))
        return student_list
    
    def __str__(self):
        return f"{self.role}: {self.name}"
