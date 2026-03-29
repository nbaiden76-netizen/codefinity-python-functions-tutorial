prices = [210, 0, -891, 432, 256]

apply_tax = lambda price: max(price, 0) * 0.87   # Deducting 13% tax

final_prices = [apply_tax(price) for price in prices]

# Testing the result
print(final_prices)

# lambda functions are anonymous fuctions 
# basic syntax lambda arguments:expression 

#square = lambda x: x**2
#result = square(5)
# print(result) 