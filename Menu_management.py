def add_item(menu, item):
    menu.append(item)
    return menu
def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
        return menu
    else:
        return f"The specified item-{item} is not present in the menu!"
def check_item(menu, item):
    if item in menu:
        return f"Item-{item} is present in the menu"
    else:
        return f"The item {item} is not present in the menu"
print("Enter the menu items one by one if done type 'done'!!")
initial_menu=[]
while True:
    menu_item=input("Enter the item_name:")
    if menu_item.lower()=='done':
        break
    initial_menu.append(menu_item)
print("\n Initial Menu:",initial_menu)
item_add=input("Enter the item name that is to be added to the menu:")
item_remove=input("Enter the item name that's got to be removed:")
item_check=input("Enter the name of the item that is to be checked for availability")
updated_menu=add_item(initial_menu,item_add)
updated_menu=remove_item(updated_menu,item_remove)
print("\nupdated menu:",updated_menu)
print(check_item(updated_menu,item_check))
