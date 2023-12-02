num_items = int(input("Number of items : "))
total_price = 0

for number in range(num_items):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > 100:
    discount = total_price * 0.1 # 10%discount
    total_price -= discount

print(f"Total price for {num_items} items is ${total_price:.2f}")