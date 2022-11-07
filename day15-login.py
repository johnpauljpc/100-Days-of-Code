def login():
  while True:
    uname = input("enter your username: ")
    pword = input("kindly enter your password: ")
    print()
    if (uname == "johnpaul" and pword == 'mypass'):
      print("Welcome ", uname)
      break
    else:
      print("Please enter valid details to get authorized!")
      continue;


print("Simple Login System")
print()
login()
