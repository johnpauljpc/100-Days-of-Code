import os, time
toDoList = []

def printList():
  print()
  for item in toDoList:
    print(item)
  print()

while True:
  menu = input("ToDoList Manager\n\nDo you want to view, add, remove or edit the todo list?\n")
  if menu=="view":
    printList()
  elif menu=="add":
    item = input("What do you want to add?\n")
    toDoList.append(item)
  elif menu=="remove":
    item = input("What do you want to remove?\n")
    if item in toDoList:
      toDoList.remove(item)
  elif menu=="edit":
    item = input("What do you want to edit?\n")
    if item in toDoList:
      editted = input(f"make the changes on {item} now :")
      
      toDoList.append(editted)
      toDoList.remove(item)
