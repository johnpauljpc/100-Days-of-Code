print("30 Days Down - What did you think?")
print()


for i in range(1, 31):
  
  thought = input(f"Day {i}:\n")
  print()
  if (thought == 'stop'):
    break
  else:
    
    myText = f"You thought Day {i} was"
    print(f"{myText:^35}")
    print(f"{thought:^35}")
    print()
    print("to end type stop")
print("****     the End      ****")

# alignment attributes:
# center is ^
# right is >
# left is <

