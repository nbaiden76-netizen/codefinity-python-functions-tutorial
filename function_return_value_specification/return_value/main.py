def merge_shopping_lists(*shopping_lists):
    merged_list = ''
    
    # Iterate through all shopping lists and combine them into a single string
    for items in shopping_lists:
        merged_list += ', '.join(items) + ', '

    return merged_list.strip(', ')

# Example usage
alice_list = ['Bread', 'Milk', 'Eggs']
bob_list = ['Meat', 'Potatoes']
charlie_list = ['Fruits', 'Juice']

# Testing the result
final_shopping_list = merge_shopping_lists(alice_list, bob_list, charlie_list)
print(final_shopping_list)



#def add_numbers(a, b):
 #   return a + b

#result = add_numbers(3, 5)
#print(result)  # outputs: 8


# Example of join()
#words = ["red", "green", "blue"]
#combined = ", ".join(words)
#print(combined)

# Example of strip()
#raw_text = ",a,b,c,"
#cleaned_text = raw_text.strip(',')
#print(cleaned_text)




