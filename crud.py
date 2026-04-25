list = []

while True:
    print("1. Add an item")
    print("2. View the list")
    print("3. Delete")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        list.append(item)

    elif choice == 2:
        for i, t in enumerate(list):
            print(i,t)
    elif choice==3:
        a=int(input("Enter index to delete: "))
        list.pop(a)

    elif choice==4:
        break


