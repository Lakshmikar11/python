list = []

while True:
    print("1. Add an item")
    print("2. Update list")
    print("3. View the list")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        list.append(item)

    if choice == 2:
        index = int(input("Enter index to update: "))
        value = input("Enter new value: ")
        list[index] = value

    elif choice == 3:
        for i, t in enumerate(list):
            print(i,t)
    elif choice==4:
        a=int(input("Enter index to delete: "))
        list.pop(a)

    elif choice==5:
        break


