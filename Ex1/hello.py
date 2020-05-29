def greet_user(first_name,last_name, age = 25):
    # Display a simple greeting
   return (f"hello!{first_name.title()} {last_name.title()}, {age}")

full_name = greet_user('villoz', 'seb',32)
print(full_name)