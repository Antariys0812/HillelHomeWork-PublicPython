class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, team_size, **kwargs):
        super().__init__(**kwargs)
        self.team_size = team_size

    def __str__(self):
        return f'name: {self.name}, salary: {self.salary}, department: {self.department}, programming_language: {self.programming_language}, team_size: {self.team_size}'

teamlead1 = TeamLead(name='John', salary=20000, department='Programming', programming_language='Python', team_size=3)
print(teamlead1)
