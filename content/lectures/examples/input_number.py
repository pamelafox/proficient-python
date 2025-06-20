def input_number(message):
  while True:
    try:
       user_input = int(input(message))
    except ValueError:
       print("Your answer must be a number. Try again.")
       continue
    else:
       return user_input
