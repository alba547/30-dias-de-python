dog = {} #1
dog = {"name": "Nila", "color": "black", "breed": "bodeguero", "legs": 4, "age": 7} #2
student_dictionary = {
    "fist_name": "Alba",
    "last_name": "Jimenez",
    "gender": "F",
    "age": 16,
    "marital_status": "single",
    "skills": "cooking",
    "country": "Spain",
    "city": "Jerez",
    "Address": 11405
} #3
print(len(student_dictionary)) #4
print(student_dictionary["skills"]) #5
print(type(student_dictionary["skills"])) 
student_dictionary["skills"].append("reading")#6
dictionary_keys = list(student_dictionary.keys()) #7
dictionary_values = list(student_dictionary.values()) #8
list_of_tuples = student_dictionary.items() #9
student_dictionary.pop("Jerez") #10
del student_dictionary #11