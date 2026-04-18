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
    print(f"\nExpense Entry {entry + 1}")
    cat_no = int(input("Enter category number (1-5) or 0 to skip: "))

    if cat_no == 0:
        continue

    if 1 <= cat_no <= 5:
        description = input("Item description: ").strip()
        amount = float(input("Amount spent: "))

        cat_name = categories[cat_no - 1][0]

        tag = ""
        if amount > (budget * 0.25):
            tag = "! High Expense Alert!"

        expenses.append([cat_name, description, amount, tag])
        total_spent += amount
    else:
        print("Invalid category. Slot skipped.")