def cart_Price(cart_items):
    if not cart_items:
        return "The cart is empty!"
    total_sum=sum(cart_items.values())
    if len(cart_items)>5:
        total_sum*=0.9
    return f"Total Price: {total_sum}"
def get_cartProds():
    cart_items={}
    while True:
        item_name=input("Enter the name of the item or enter exit:")
        if item_name=="exit":
            break
        try:
            item_price=float(input(f"Enter the price of {item_name} :"))
            cart_items[item_name]=item_price
        except ValueError:
            print("Please enter a valid price.")
    return cart_items
cart_items=get_cartProds()
print(cart_Price(cart_items))