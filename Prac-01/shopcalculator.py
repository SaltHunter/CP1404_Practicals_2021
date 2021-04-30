def main():
    items = int(input("Input the number of items here"))
    total = 0
    i = 0
    for i in range(1, items + 1):
        print("Price of item", i,)
        price = float(input("Input the price of items here"))
        total += price
    if total > 100:
        print("The total price is", i, "item is", total * 0.9)
main()