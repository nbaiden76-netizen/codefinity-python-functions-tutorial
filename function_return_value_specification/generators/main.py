def id_generator():
    # when initialising the value no need to put it in bracdkets 
    count = 1
    while True:
        yield f"ID_{count}"
        count += 1

id_gen = id_generator()

# Testing the result
for _ in range(5):
    unique_id = next(id_gen)
    print(unique_id)


#def unique_logins_from_list(login_list):
    # Iterate over each login in the list
 #   for login in login_list: 
  #      yield login  # `yield` the current login

# A predefined list of available logins
#login_list = ["user1", "user2", "user3", "user4", "user5"]

# Creating a generator instance from the login list
#login_generator = unique_logins_from_list(login_list)

# Generate and print 5 logins, one at a time
#for _ in range(5):
    # Each call to `next()` gives the next login
  #  print(next(login_generator)) 
