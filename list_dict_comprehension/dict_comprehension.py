import random

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ["ben", "tom", "gabriel", "raphael"]

# students={<new_key>:<new_value> for <item> in <ITERABLE>}
# students={<new_key>:<new_value> for (key,value) in <ITERABLE>}

students = {student: random.randint(20, 100) for student in names}
print(students)

passed_students = {name: score for (name, score) in students.items() if score > 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

word_count_map={word:len(word) for word in sentence.split(" ")}
print(word_count_map)