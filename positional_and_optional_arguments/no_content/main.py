users_db = []
# Note user_db is set as empty 

# Here we define the function 
def register_user(username, email, age):
# here we check the age via an if statement 
    if age < 18:
        return "Registration failed: age must be 18 or older."

# Here we create a dictionary using Key and values 
    user = {"username": username, "email": email, "age": age}
    # Adding the User dictionary to the User_db 
    users_db.append(user)
    
    return f"User {username} registered successfully!"

# Pass the parameters in any way to register a user
result1 = register_user(email='bills.matters@cost.com', username='madprofessor', age=50)
# below users Postioning for the function 
result2 = register_user('madprofessor', 'bills.matters@cost.com', 50)

# Testing the result
print(result1)
print(result2)
print(users_db)  # List of registered users
