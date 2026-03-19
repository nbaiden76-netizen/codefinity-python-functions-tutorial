def describe_dog(name, breed, age):
    # Check if the age is valid
    if age < 0:
        return f"Invalid age for {name}. Age cannot be negative." 
    # Check if the dog is a newborn
    elif age == 0:
        return f"{name} is a newborn {breed}. A bundle of joy!"
    # Check if the dog is 1 year old
    elif age == 1:
        return f"{name} is a 1-year-old {breed}. A great companion!"
    # For all other ages, including plural years
    else:
        return  f"{name} is a {age}-year-old {breed}. An old dog with much wisdom!"

# Test the function with various scenarios
description = describe_dog("Buddy", "Labrador", 3)
print(description)



#def walk_the_dog(dog_name, walk_time):
    # Check if the walk time is between 6 and 18 hours
#    if 6 <= walk_time <= 18:
 #       return f"Time to walk {dog_name}!"
 #   else:
#        return f"Wait until 6 PM to walk {dog_name}!"

# Function calls with different parameters
#message1 = walk_the_dog("Bella", 14)
#message2 = walk_the_dog("Charlie", 20)

# Display the results
#print(message1)
#print(message2)