
class Student:
    def __init__(self, first_name:str, last_name:str, gpa:float,
                 credits:int, bannerid:int = None):
        self.bannerid = bannerid
        self.first_name = first_name
        self.last_name = last_name
        if gpa >4 or gpa<0:
            raise ValueError
        self.gpa = gpa
        self.credits = credits


    def __str__(self):
        return f"""Student Object with 
BannerID: {self.bannerid}
Name: {self.first_name} {self.last_name}
Credits: {self.credits}
GPA: {self.gpa}"""


    def __lt__(self, other:'Student'):
        return self.gpa < other.gpa


