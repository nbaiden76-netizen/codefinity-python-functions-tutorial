def filter_products_by_budget(budget, **kwargs):
    affordable_products = {} 
    for product, price in kwargs.items():
        if budget >= price:
            affordable_products[product] = price
            
    # utilising  'not' is important here 
    if not affordable_products:
        return "No products available within the budget."
    
    return f"Available products within budget: {affordable_products}"

# Testing the result
print(filter_products_by_budget(100, laptop=1200, smartphone=800, mouse=50, keyboard=90, headphones=150))


#def example_function(**kwargs):
 #   for key, value in kwargs.items():
#        print(f'{key}: {value}')

# Example function call
#example_function(name='John', age=25, city='New York')