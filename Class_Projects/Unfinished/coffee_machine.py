
#resources----------------------------------------------------------------------

machine_resources = {
    "water" : 300,
    "milk" : 200,
    "coffee" : 100,
    "money" : 0.0
}

menu_options = {
    "espresso" : {
        'water': 50,
        "coffee": 18,
        "price":1.50
    },
    "latte": {
        'water': 200,
        'coffee': 24,
        'milk': 150,
        "price":2.50
    },
    "cappucino":{
        'water': 250,
        'coffee': 24,
        'milk': 100,
        "price":3.00
    }

    
}

currency = {
    "penny": 0.01,
    "nickel":0.05,
    "dime": 0.10,
    "quarter": 0.25,
    "dollar":1.00
}

#methods--------------------------------------------------------------------------------

def print_report(machine_resources= machine_resources)  :
    for item in machine_resources:
        print(item,"has about",machine_resources[item])

def print_menu(menu = menu_options):
    print("---MENU---\n")
    for item in menu_options:
        for attribute in (menu_options[item]):
            if attribute == "price":
                print(item,":",(menu_options[item][attribute]),"$\n")
            
      





def choice(choice):
    if choice == "espresso":
        if machine_resources["water"] >= menu_options["espresso"]["water"] and machine_resources["coffee"] >= menu_options["espresso"]["coffee"]:
            print("yes")
        else:
            print("nope")
    elif choice == "latte":
        if machine_resources["water"] >= menu_options["latte"]["water"] and machine_resources["coffee"] >= menu_options["latte"]["coffee"] and machine_resources["milk"] >= menu_options["latte"]["milk"]:
            print("yes")
        else:
            print("nope")
    elif choice == 'cappucino':
        if machine_resources["water"] >= menu_options["cappucino"]["water"] and machine_resources["coffee"] >= menu_options["cappucino"]["coffee"] and machine_resources["milk"] >= menu_options["cappucino"]["milk"]:
            print("yes")
        else:
            print("nope")
    else:
        print("Not a valid choice")
        
def take_payment(pennies,nickels,dimes,quarters,dollars):

#main --------------------------------------------------------------------------------
def main():
    print("Welcome To The Coffee Machine\n")
    print_menu()
    choice(choice = input("What would you like to drink: "))






main()