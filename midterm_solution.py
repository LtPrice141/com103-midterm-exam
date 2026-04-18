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

