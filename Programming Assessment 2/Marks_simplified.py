print("Please enter your 5 marks below")

# create array/list with five marks
valid_marks_list = []
for each_mark in range(5):
    valid_entry = False
    while not valid_entry:
        try:
            mark = int(input(f"Enter mark {each_mark + 1}: "))
            if 0 <= mark <= 100:
                valid_marks_list.append(mark)
                valid_entry = True
            else:
                print("\033[91mThe number you entered is out of the range (0-100)")
        except ValueError:
            print("\033[91mInvalid entry. The mark must be a number")

# print the array/list
print(valid_marks_list)

# calculate the sum and average
sumOfMarks = sum(valid_marks_list)
averageOfMarks = sum(valid_marks_list) / 5

# display results
print("The sum of your marks is: " + str(sumOfMarks))
print("The average of your marks is: " + str(averageOfMarks))
