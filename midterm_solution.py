print("=" * 40)
print("\tSTUDENT WEEKLY BUDGET TRACKER")
print("=" * 40)
print()
 
student = input("Student name: ").title()
budget = float(input("Weekly budget (number): "))

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

