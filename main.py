sandwich_orders = ["tuna", "chicken", "Ham" ]
sandwich_finished = [ ]

while len(sandwich_orders) > 0:
    sandwich_finished.append(sandwich_orders[0])
    sandwich_orders.remove(sandwich_orders[0])
    print(f"The {sandwich_finished[-1]} Sandwich ready")

print(f"\nThe following sandwiches were made:")
print(*sandwich_finished)

