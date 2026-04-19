print("=" * 52)
print("\t   STUDENT WEEKLY BUDGET TRACKER")
print("=" * 52)
print()

student_name = input("Enter your name: ").title()
while True:
    weekly_budget = input("Enter your Weekly Budget: ")

    if weekly_budget.replace('.', '', 1).isdigit():
        weekly_budget = float(weekly_budget)
        break
    else:
        print("Invalid input. Please enter a number.")

print()

categories = [
    ["Food & Drinks", "Lunch, snacks, coffee"],
    ["Transportation", "Bus, jeepney, ride-share"],
    ["Mobile / Internet", "Load, data plan, WiFi top-up"],
    ["School Supplies", "Notebook, pen, bond paper"],
    ["Entertainment", "Games, movies, hangout"]
]

print("=" * 52)
print("\t   WEEKLY EXPENSE -- CATEGORIES")
print("=" * 52)
print(f"{'No':<3} {'Category':<20} {'Example Expenses'}")
print()

for index, category in enumerate(categories, 1):
    print(f"{index:<3} {category[0]:<20} {category[1]}")
print("=" * 52)
print()

expenses = []
total_spent = 0

for entry in range(4):
    print(f"\n--- Expense Entry {entry + 1} ---")
    print()
    while True:
        raw_category = input(
            "Enter category number (1-5) or 0 to skip: ").strip()
        if raw_category.isdigit():
            category_number = int(raw_category)
            if 0 <= category_number <= 5:
                break
        print("Invalid input. Please enter a number from 0 to 5.\n")

    if category_number == 0:
        continue

    description = input("Item description: ").strip()

    while True:
        raw_amount = input("Amount spent: ").strip()
        if raw_amount and raw_amount.replace(".", "", 1).isdigit() and raw_amount.count(".") <= 1:
            amount = float(raw_amount)
            if amount >= 0:
                break
        print("Invalid input. Please enter a valid amount (e.g., 75 or 75.50).\n")

    category_name = categories[category_number - 1][0]

    tag = ""
    limit = weekly_budget * 0.25
    if amount > limit:
        tag = "! High Expense Alert!"

    expenses.append([category_name, description, amount, tag])
    total_spent += amount

remaining = weekly_budget - total_spent
status = "Budget OK! Keep it up." if remaining >= 0 else "Overspent! Reduce spending."

print("\n" + "=" * 54)
title = f"{student_name.upper()} -- WEEKLY EXPENSE LOG"
print(f"{title:^54}")
print("=" * 54)

print(f"  Weekly Budget  : P{weekly_budget:.2f}")

description_width = 38
amount_width = 8

for i in range(1, 6):
    category_name = categories[i - 1][0]

    items = []
    for item in expenses:
        if item[0] == category_name:
            items.append(item)

    if items:
        print(f"  [{i}] {category_name:<20}")
        for entry in items:
            description = entry[1]
            amount = entry[2]
            tag = entry[3]

            if len(description) > description_width:
                description = description[:description_width - 3] + "..."

            alert = "  ! High Expense Alert!" if tag else ""

            print(
                f"      {description:<{description_width}} P{amount:>{amount_width}.2f}{alert}")

print("-" * 54)

print(f"  Total Spent    : P{total_spent:>8.2f}")
print(f"  Remaining      : P{remaining:>8.2f}")
print(f"  Status         : {status}")
print("=" * 54)
