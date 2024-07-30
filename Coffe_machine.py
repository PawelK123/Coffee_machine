import Menu
is_on = True
resources = Menu.resources
profit = 0
while is_on == True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        is_on = False
        break
    menu = Menu.MENU
    ingredients1 = menu[choice]
    ingredients = ingredients1['ingredients']
    cost = ingredients1['cost']

    def money(profit):
        print("Please insert your coins.")
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.1
        nickles = int(input("How many nickles? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        total = quarters + dimes + nickles + pennies
        return total

    total = money(profit)
    list_of_things = ["water","milk","coffee"]


    def checking_ingredients(ingriedients,resources,total,cost):
        for i in list_of_things:
            if ingriedients[i] > resources[i]:
                return print(f"Sorry i can't make a coffe. I don't have enough {i}")
            elif cost > total:
                return print(f"Sorry that's not enough money. It's cost ${cost} and you have ${total}. Money refunded")
            else:
                change = total - cost
                change = round(change,2)
                return change



    change = checking_ingredients(ingredients,resources,total,cost)
    if isinstance(change, (int, float)):
        print(f"Here is ${change} in change")
        print("Here is your espresso 🍮. Enjoy!")
        profit += change

    def report(ingredients,resources):
        list_left_resources = {}
        for i in list_of_things:
            list_left_resources[i] = (resources[i] - ingredients[i])
        return list_left_resources


    if isinstance(change, (int, float)):
        list_left_resources = report(ingredients, resources)
    report = input("Do you want report of resources? Type 'y' or 'n' ").lower()
    if report == 'y':
        print(f"{list_left_resources}, money ${profit}")
    resources = list_left_resources
