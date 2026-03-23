def calculate_total(*prices):
    # 1. Empty Cart Check 
    if not prices:
        return "Your cart is empty."
        
    #2. Sum the prices 
    total = sum(prices)

    if total >= 200:
        total *= 0.8  # 20% discount
    elif total >= 100:
        total *= 0.9  # 10% discount

    return f"Final total: ${total:.2f}"

# Testing the result
print(calculate_total(30, 20, 50))
print(calculate_total(100, 50, 80))
print(calculate_total(150, 100))
print(calculate_total())

# Define function with arbitrary positional arguments named values
#def calculate_sum(*values):
#    return sum(values)

# Test the function using different number of arguments
#print(calculate_sum(1, 2, 3))
#print(calculate_sum(1, 2, 3, 4))
#print(calculate_sum(1, 2, 3, 4, 5))




#def example_function(*args):
#    print(type(args))
#    print(args)
#    for arg in args:
#        print(arg)

#print("Call without arguments:")
#example_function()

#print("\nCall with one argument:")
#example_function(1)

#print("\nCall with multiple arguments:")
#example_function(1, 2, 3, 'hello', [4, 5, 6])