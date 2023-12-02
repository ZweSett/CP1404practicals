import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = 'stock_simulation_output.txt'

# Open the file for writing
out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
days = 0

print(f"Starting price: ${price:,.2f}")
print(f"Writing simulation results to: {OUTPUT_FILE}\n")

while MIN_PRICE <= price <= MAX_PRICE:
    days += 1
    price_change = 0

    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)

    # Print to console
    print(f"On day {days} price is: ${price:,.2f}")

    # Print to file
    print(f"On day {days} price is: ${price:,.2f}", file=out_file)

    # Check if the price is out of bounds
    if price > MAX_PRICE or price < MIN_PRICE:
        break

# Close the file
out_file.close()