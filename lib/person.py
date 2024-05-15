#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]


class Person:
    def __init__(self, name="None", job="None"):
        self.name = name  # we are calling a method
        self.set_job(job)

    # def get_name(self):
    #     return self._name

    # def set_name(self, name):
    #     # Check if name is a string and its length is between 1 and 25 characters
    #     if not isinstance(name, str) or not (1 <= len(name) <= 25):
    #         print("Name must be string between 1 and 25 characters.")
    #     else:
    #         self._name = name.title()

    # name = property(get_name, set_name)
    # p = Person(1, "manager")
    # p.name = 2

    # p = Person()
    # p.__init__(1, "manager")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        # if empty string
        # if not a string
        # if string over 25 characters
        # print("in setter")
        # Check if name is a string and its length is between 1 and 25 characters
        if name == '':
            print('Name must be string between 1 and 25 characters.')
        elif not isinstance(name, str):
            print("Name must be string between 1 and 25 characters.")
        elif not (1 <= len(name) < 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = name.title()

    def get_job(self):
        return self._job

    def set_job(self, job):
        # Check if job is in the list of approved jobs
        # print("in setter")
        if job not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = job

    job = property(get_job, set_job)
