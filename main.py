sandwich_orders = ["tuna", "chicken", "Ham"]
sandwich_finished = [ ]



while len(sandwich_orders) > 0:
    sandwich_finished.append(sandwich_orders[0])
    sandwich_orders.remove(sandwich_orders[0])
    print(f"your {sandwich_orders[0]} is ready")
    

