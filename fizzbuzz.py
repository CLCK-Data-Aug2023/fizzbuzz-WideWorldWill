for digits in range(1,101):
  if digits % 5 == 0 and digits % 3 == 0:
    print("FizzBuzz")
  elif digits % 5 == 0:
    print("Buzz")
  elif digits % 3 == 0:
    print("Fizz")
  else:
    print(digits)
