running = True

to_do_list = []
# v 1.0
# while running:
#     item = input("What do want to add? ")
#     to_do_list.append(item)
#     cont = input("Do you wish to add another item? (Y/N) ")
#
#     if cont == 'Y': running = True
#     else: running = False
#
# print("You have the following to do: {}".format(", ".join(to_do_list)))


# v 2.0
def show_items():
    print("You have the following to do: \n {}\n".format("\n".join(to_do_list)))
def show_help():
    print("\nEnter an item to add it to the list. Enter \'DONE\' to exit the application and \'SHOW\' to view your list. \'HELP\' will bring up this text. \n")

while running:
    item = input("Please enter an item: ")
    if item == 'DONE':
        running = False
        show_items()
    elif item == 'SHOW':
        show_items()
    elif item == 'HELP':
        show_help()
    else:
        to_do_list.append(item)
