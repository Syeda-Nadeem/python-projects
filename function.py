def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = hotel_rate * trip_time - 10
    print("Total expense is", car_rental_total +
          hotel_total + plane_ticket_price, "dollars")


calculate_expenses(200, 100, 100, 5)


# function with multiple args.
# Difrent types of args
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
    print("Here is what your trip will look like!")
    print("First, we will stop in " + first_destination + ", then " +
          second_destination + ", and lastly " + final_destination)


trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner("Iceland", "Germany", "India")
trip_planner("Brooklyn", "Queens")

# built in functions
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price)
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price)
rounded_price = round(tshirt_price)
print(rounded_price)

# This function will print a hardcoded count of how many locations we have.
favorite_locations = "Paris, Norway, Iceland"


def print_count_locations():
    print("There are 3 locations")

# This function will print the favorite locations


def show_favorite_locations():
    print("Your favorite locations are: " + favorite_locations)


print_count_locations()
show_favorite_locations()

# return
current_budget = 3500.75


def print_remaining_budget(budget):
    print("Your remaining budget is: $" + str(budget))


print_remaining_budget(current_budget)

# Write your code below:


def deduct_expense(budget, expense):
    return budget - expense


shirt_expense = 9

new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)
