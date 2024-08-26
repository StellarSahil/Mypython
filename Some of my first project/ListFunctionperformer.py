l1 = []

def sort_list():
    l1.sort()

def reverse_list():
    l1.reverse()

def add_to_list():
    n = input("Enter what you want to add: ")
    y = int(input("Is your entered value an integer? \nPress 1 for Yes or 0 for No: "))
    if y == 1:
        n = int(n)  # Convert to int if specified
    l1.append(n)

def add_at_index():
    n = input("Enter what you want to add: ")
    y = int(input("Is your entered value an integer? \nPress 1 for Yes or 0 for No: "))
    if y == 1:
        n = int(n)  # Convert to int if specified
    print(l1)
    k = int(input(f"At which index do you want to add \"{n}\": "))
    l1.insert(k, n)

def remove_from_list():
    n = input("Enter the value you want to remove: ")
    y = int(input("Is the value an integer? \nPress 1 for Yes or 0 for No: "))
    if y == 1:
        n = int(n)  # Convert to int if specified
    if n in l1:
        l1.remove(n)
    else:
        print(f"{n} is not in the list")

a = -1
print("What would you like to do with the List?")
while a != 0:
    print('''
Press 1 to sort the list
Press 2 to reverse the list
Press 3 to add something to the list
Press 4 to add something at a specific index
Press 5 to remove something from the list
Press 0 to exit 
          ''')
    a = int(input("Enter your choice: "))
    if a == 1:
        sort_list()
    elif a == 2:
        reverse_list()
    elif a == 3:
        add_to_list()
    elif a == 4:
        add_at_index()
    elif a == 5:
        remove_from_list()
    elif a == 0:
        break
    else:
        print(f"The choice {a} is not valid.")
    print("Current List:", l1)

print("Final List:", l1)
