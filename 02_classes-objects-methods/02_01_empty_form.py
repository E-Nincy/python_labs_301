# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.

class MedicalForm:
    def __init__(self, name, age, gender , symptoms, allergies):
        self.name = name
        self.age = age
        self.gender = gender
        self.symptoms = symptoms
        self.allergies = allergies

    def __str__(self):
        return (f"Patient: {self.name}, Age: {self.age}, Gender: {self.gender}, "
                f"Symptoms: {self.symptoms}, Allergies: {self.allergies}")
    
# Create form (objects)
patient1 = MedicalForm("Ana Garcia", 28, "Female", "Headache, fever", "None")
patient2 = MedicalForm("Simon Baumhauer", 29, "Male", "Back pain", "Ibuprofen")
patient3 = MedicalForm("Roxana Romero", 35, "Female", "Fatigue, cough", "Dust")

# Prit form and Object
print(patient1)
print(patient2)
print(patient3)