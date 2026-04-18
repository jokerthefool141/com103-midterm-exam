print("=" * 40)
print("\tSTUDENT WEEKLY BUDGET TRACKER")
print("=" * 40)
print()
 
student = input("Student name: ").title()
raw = input("Weekly budget (whole number): ").strip()
print()

while not raw.isdigit():
    print("Invalid input. Please enter a whole number (e.g., 500).\n")
    raw = input("Weekly budget (whole number): ").strip()

budget = float(raw)

print()

categories = [
    ["Food & Drinks", "Lunch, snacks, coffee"],
    ["Transportation", "Bus, jeepney, ride-share"],
    ["Mobile / Internet", "Load, data plan, WiFi top-up"],
    ["School Supplies", "Notebook, pen, bond paper"],
    ["Entertainment", "Games, movies, hangout"]
]

print("=" * 50)
print("\t  WEEKLY EXPENSE -- CATEGORIES")
print("=" * 50)
print(f"{'No':<3} {'Category':<20} {'Example Expenses'}")
print()

for i, cat in enumerate(categories, 1):
    print(f"{i:<3} {cat[0]:<20} {cat[1]}")
print("=" * 50)
print()

expenses = []
total_spent = 0

for entry in range(4):
    print(f"\n--- Expense Entry {entry + 1} ---")
    print()
    category_number = int(input("Enter category number (1-5) or 0 to skip: "))

    if category_number == 0:
        continue

    if 1 <= category_number <= 5:
        description = input("Item description: ").strip()
        amount = float(input("Amount spent: "))

        category_name = categories[category_number - 1][0]

        tag = ""
        if amount > (budget * 0.25):
            tag = "! High Expense Alert!"

        expenses.append([category_name, description, amount, tag])
        total_spent += amount
    else:
        print("Invalid category. Slot skipped.")

remaining = budget - total_spent
if remaining >= 0:
    status = "Budget OK! Keep it up."
else:
    status = "Overspent! Reduce spending."

print("\n" + "=" * 55)
print(f"{'WEEKLY EXPENSE REPORT':^55}")
print("=" * 55)
print(f"Student Name : {student}")
print(f"Weekly Budget: P{budget:.2f}")
print("-" * 55)

if len(expenses) == 0:
    print("No expenses logged.")
else:
    print(f"{'No':<3} {'Category':<18} {'Description':<18} {'Amount':>8}")
    print("-" * 55)
    count = 1
    for category_name, description, amount, tag in expenses:
        print(f"{count:<3} {category_name:<18} {description:<18} P{amount:>7.2f}")
        if tag != "":
            print(f"    {tag}")
        count += 1
    print("-" * 55)

print(f"{'Total Spent:':<20} P{total_spent:>32.2f}")
print(f"{'Remaining:':<20} P{remaining:>32.2f}")
print(f"Status: {status}")
print("=" * 55)
