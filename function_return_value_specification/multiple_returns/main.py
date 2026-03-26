def validate_registration(username, email, password): # whats key to remember is that Parameters go in the brackets 
    
    errors = []

    if len(username) < 3:
        errors.append("Username must be at least 3 characters long.")
    if "@" not in email:
        errors.append("Invalid email format.")
    if len(password) < 6:
        errors.append("Password must be at least 6 characters long.")

    return len(errors) == 0, errors

# Testing the result
is_valid, errors = validate_registration("js", "userexample.com", "123")
print("Validation successful:", is_valid)
print("Errors:", errors)



# Define a function
#def return_multiple_objects():
 #   obj1 = 'Hello'
#    obj2 = 42
#    obj3 = [1, 2, 3]
    # Return all objects packed into list
 #   return [obj1, obj2, obj3]
  
# Get the list with corresponding objects
#result_list = return_multiple_objects()
#for obj in result_list:
#    print(obj)


#def return_multiple_objects():
#    obj1 = "Hello"
#    obj2 = 42
#    obj3 = [1, 2, 3]
    # Return objects separated by comma
#    return obj1, obj2, obj3

# Get the result of the function into three different values
#result1, result2, result3 = return_multiple_objects()
#print(result1, result2, result3)