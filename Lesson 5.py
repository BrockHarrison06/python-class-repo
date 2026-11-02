import random 

def main(): grades = [] 

while True: 
    grade = int(input("Enter a grade or -1 to stop: ")) 
    if grade == -1: 
        break 
    else: 
        grades.append(grade) 
 
print("\nGrades entered:", grades) 
 
if len(grades) == 0: 
    print("No grades were entered.") 
    print("Completed by, Brock Harrison") 
    return 
 
print("\n--- Removing the Lowest Grade ---") 
lowest_grade = min(grades) 
lowest_index = grades.index(lowest_grade) 
grades.pop(lowest_index) 
print("Grades:", grades) 
 
if len(grades) == 0: 
    print("\nNot enough grades remain to remove a random grade or edit a grade.") 
    print("Completed by, Brock Harrison") 
    return 
 
print("\n--- Removing a Random Grade ---") 
random_grade = random.choice(grades) 
grades.remove(random_grade) 
print("Grades:", grades) 
 
if len(grades) == 0: 
    print("\nNo grades remain to edit or calculate an average.") 
    print("Completed by, Brock Harrison") 
    return 
 
print("\n--- Edit a Grade ---") 
for index, grade in enumerate(grades, start=1): 
    print(f"{index}. {grade}") 
 
grade_number = int(input("Which grade would you like to edit? Enter its number: ")) 
while grade_number < 1 or grade_number > len(grades): 
    print("Error: please enter a number from 1 to", len(grades)) 
    grade_number = int(input("Which grade would you like to edit? Enter its number: ")) 
 
new_grade = int(input("Enter the new grade: ")) 
grades[grade_number - 1] = new_grade 
print("Grades:", grades) 
 
print("\n--- Sorting and Reversing the List ---") 
grades.sort() 
grades.reverse() 
print("Grades:", grades) 
 
print("\n--- Grade Total and Average ---") 
def get_total(grade_list): 
    return sum(grade_list) 
 
def get_average(grade_list): 
    return sum(grade_list) / len(grade_list) 
 
total = get_total(grades) 
average = get_average(grades) 
print("Grade total:", total) 
print("Grade average:", round(average, 2)) 
 
print("\nCompleted by, Brock Harrison") 
  

if name == "main": main() input("\nPress Enter to close this window...")