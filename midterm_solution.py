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

# ------------------ CATEGORY MENU (USING LOOP) ------------------
cat_names = [
    "Food & Drinks",
    "Transportation",
    "Mobile / Internet",
    "School Supplies",
    "Entertainment"
]

print("========== CATEGORIES ==========")
i = 0
while i < len(cat_names):
    print(str(i + 1) + ". " + cat_names[i])
    i = i + 1
print("================================")
print("")

# ------------------ STORAGE ------------------
log_cat = []
log_desc = []
log_amt = []

total_spent = 0

# ------------------ EXPENSE LOOP ------------------
i = 1
while i <= 4:
    print("--- EXPENSE " + str(i) + " ---")

    # CATEGORY INPUT
    while True:
        cat_input = input("Category (1-5, 0 to skip): ")

        valid = True

        if cat_input == "":
            valid = False
        else:
            for ch in cat_input:
                if ch < "0" or ch > "9":
                    valid = False

        if valid == True:
            cat = int(cat_input)
            if cat >= 0 and cat <= 5:
                break
            else:
                valid = False

        if valid == False:
            print("Invalid category. Enter 0 to 5 only.")

    if cat == 0:
        print("Skipped.")
        print("")
        i = i + 1
    else:
        # DESCRIPTION INPUT
        while True:
            desc = input("Description: ")
            if desc == "":
                print("Invalid input. Description cannot be empty.")
            else:
                break

        # AMOUNT INPUT
        while True:
            amt_input = input("Amount: ")

            valid = True

            if amt_input == "":
                valid = False
            else:
                for ch in amt_input:
                    if ch < "0" or ch > "9":
                        valid = False

            if valid == True:
                amount = int(amt_input)
                break
            else:
                print("Invalid input. Enter a number only.")

        # STORE
        log_cat.append(cat)
        log_desc.append(desc)
        log_amt.append(amount)

        total_spent = total_spent + amount

        print("")
        i = i + 1

# ------------------ FINAL REPORT ------------------
remaining = weekly_budget - total_spent

print("")
print("========================================")
print(name + " - WEEKLY EXPENSE LOG")
print("========================================")
print("Weekly Budget: P" + str(weekly_budget))
print("")

# PRINT LOG SEQUENTIALLY
i = 0
while i < len(log_cat):
    cat_name = cat_names[log_cat[i] - 1]
    amount = log_amt[i]

    line = str(i + 1) + ". [" + cat_name + "] " + log_desc[i] + " - P" + str(amount)

    if amount > weekly_budget * 25 / 100:
        line = line + "  ! High Expense Alert !"

    print(line)

    i = i + 1

print("----------------------------------------")
print("Total Spent: P" + str(total_spent))
print("Remaining Balance: P" + str(remaining))

# STATUS
if remaining >= 0:
    print("Status: Budget OK! Keep it up.")
else:
    print("Status: Overspent! Reduce spending.")

print("========================================")