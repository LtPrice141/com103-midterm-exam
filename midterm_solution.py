# WEEKLY STUDENT EXPENSE TRACKER

# ------------------ NAME INPUT ------------------
while True:
    name = input("Enter student name: ")

    if name == "":
        print("Invalid input. Name cannot be empty.")
    else:
        valid = True
        for ch in name:
            if ch == " ":
                valid = False
        if valid == True:
            break
        else:
            print("Invalid input. No spaces allowed.")

# ------------------ BUDGET INPUT ------------------
while True:
    budget_input = input("Enter weekly budget: ")

    valid = True

    if budget_input == "":
        valid = False
    else:
        for ch in budget_input:
            if ch < "0" or ch > "9":
                valid = False

    if valid == True:
        weekly_budget = int(budget_input)
        break
    else:
        print("Invalid input. Please enter a number.")

print("")
print("Student name:", name)
print("Weekly budget:", weekly_budget)
print("")

