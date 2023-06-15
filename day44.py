import os

listOfShame = [] 

while True: 
  menu = input("Add or Remove or Exit? \n press a to add, r to remove, q or e to exit:  ") 

  if(menu.strip().lower()[0]=="a"): 
    
    name = input("What is your name? ")
    age = input("What is your age? ")
    pref = input("What is your computer platform? ")
    
    row = [name, age, pref] 
  
    listOfShame.append(row) 
    
  elif(menu.strip().lower()[0]=='r' ):
    name = input("What is the name of the record to delete?") 
    
    for r in listOfShame:
      if name in r: 
        listOfShame.remove(r) # remove the whole row if name is in it
  elif(menu.strip().lower()[0]=='q' or menu.strip().lower()[0]=='e' ): 
    print('-------- ended ------')
    break
  else:
    os.system('cls')
    print('---Wrong Input ----')
    exit()



print(listOfShame)
