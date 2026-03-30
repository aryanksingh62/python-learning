class Student:
    count=0
    def __init__(self,name,l_marks):
        self.name=name
        self.l_marks=l_marks
        Student.count+=1
    def averageg(self):
        avg= sum(self.l_marks)/len(self.l_marks)
        return f"average of {self.name} is {avg}"
    def highest(self):
        return max(self.l_marks)
    def lowest(self):
        return min(self.l_marks)
    @classmethod
    def total_student(cls):
        return cls.count
s1 = Student("John", [80, 90, 70, 85])
s2 = Student("Sara", [90, 95, 88, 92])

print(s1.averageg())       
print(s1.highest())       
print(s1.lowest())         

print(s2.averageg())       
print(s2.highest())    
print(s2.lowest())     

print(Student.total_student())