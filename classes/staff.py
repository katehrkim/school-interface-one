import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/staff.csv")

class Staff:
    def __init__(self, name, age, role, employee_id, password):
        self.name = name 
        self.age = age         
        self.password = password
        self.role = role

    @classmethod
    def all_staff(cls):
        staff_list = []
        with open(path) as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for line in dict_reader:
                staff_list.append(cls(**line))
        return staff_list

    def __str__(self):
        return f"{self.role}: {self.name}"