name = input("Student name: ")
budget = int(input("Weekly budget: "))

print("==========================================")
print("   WEEKLY EXPENSE -- CATEGORIES")
print("==========================================")
print(" 1. Food & Drinks       [e.g. Lunch, snacks, coffee]")
print(" 2. Transportation      [e.g. Bus, jeepney, ride-share]")
print(" 3. Mobile / Internet   [e.g. Load, data plan, WiFi top-up]")
print(" 4. School Supplies     [e.g. Notebook, pen, bond paper]")
print(" 5. Entertainment       [e.g. Games, movies, hangout]")
print("==========================================")

expenses = []
total_spent = 0

for i in range(1, 5):
    print("--- EXPENSE {} ---".format(i))
    
    while True:
        cat_num = int(input("Category (0 to skip): "))
        
        if cat_num == 0:
            category_name = "Skip"
            break
        elif cat_num == 1:
            category_name = "Food & Drinks"
            break
        elif cat_num == 2:
            category_name = "Transportation"
            break
        elif cat_num == 3:
            category_name = "Mobile / Internet"
            break
        elif cat_num == 4:
            category_name = "School Supplies"
            break
        elif cat_num == 5:
            category_name = "Entertainment"
            break
        else:
            print("Invalid category. Please choose 0 to 5.")

    if cat_num == 0:
        continue

    desc = input("Description: ")
    amount = int(input("Amount: "))
    
    alert = ""
    if amount > (budget * 0.25):
        alert = " ! High Expense Alert!"
    
    expenses.append([category_name, desc, amount, alert])
    total_spent = total_spent + amount

remaining = budget - total_spent

print("======================================================")
print("     {} -- WEEKLY EXPENSE LOG".format(name.upper()))
print("======================================================")
print("  Weekly Budget  : P{}".format(budget))

count = 1
for item in expenses:
    print("  [{}] {}".format(count, item[0]))
    print("      {}              P{}{}".format(item[1], item[2], item[3]))
    count = count + 1

print("------------------------------------------------------")
print("  Total Spent    : P{}".format(total_spent))
print("  Remaining      : P{}".format(remaining))

if remaining >= 0:
    print("  Status         : Budget OK! Keep it up.")
else:
    print("  Status         : Over Budget! Be careful.")
print("======================================================")

