class Patient:
    def __init__(self,name,age,disease):
        self.name=name
        self.age=age
        self.disease=disease
        
class Doctor:
    def __init__(self,name):
        self.name=name
        self.patients=[]
    
    def add_patient(self,patient):
        self.patients.append(patient)
        print("patient added")
    
    def discharge_patient(self,patient):
        for i in self.patients:
            if i.name==patient:
                self.patients.remove(i)
                print("patient dicharged succesfully")
                return
        print("patient not found")
    # @classmethod
    def get_patient_count(self):
        return len(self.patients)
    
# Create patients
p1 = Patient("John", 25, "Fever")
p2 = Patient("Sara", 30, "Flu")
p3 = Patient("Mike", 45, "Diabetes")

# Create doctor
d = Doctor("Dr. Smith")

# Test add patients
d.add_patient(p1)
d.add_patient(p2)
d.add_patient(p3)

# Test count
print(d.get_patient_count())

# Test discharge
d.discharge_patient("Sara")
print(d.get_patient_count())

# Test patient not found
d.discharge_patient("Unknown")

# Test doctor name
print(d.name) 

# Test patient details
print(p1.name)
print(p1.age)
print(p1.disease)