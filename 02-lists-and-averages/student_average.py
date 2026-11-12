# Student average calculator

# Ask for 3 students' names and 5 marks each
# Then calculate each student's total and average mark

names = [""] * 3
total_marks = [0] * 3
average_marks = [0] * 3
marks = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for student in range(3):
    names[student] = input("Enter student name: ")

    for mark_number in range(5):
        print(f"Enter mark {mark_number + 1}: ")
        marks[student][mark_number] = int(input())
        total_marks[student] += marks[student][mark_number]

    average_marks[student] = round(total_marks[student] / 5, 1)
    print(f"Total for {names[student]}: {total_marks[student]}")
    print(f"Average mark for {names[student]}: {average_marks[student]}")

input("\nPress ENTER to exit program ")
