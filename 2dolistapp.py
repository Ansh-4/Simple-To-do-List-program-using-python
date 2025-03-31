task = []
def addTask():
  Task=input("Please enter a task you want to add: ")
  task.append(Task)
  print(f"{Task} has been successfully added")

def DisplayTask():
  if not task:
    print("There are no tasks listed currently.")
  else:
    print("Current Task: ")
    for index, item in enumerate(task):
      print(f"Task #{index}. {item}")
      
def DeleteTask():
  DisplayTask()
  try:
   Select= int(input("Please enter the task number you want to delete: "))
   if Select>=0 and Select<len(task):
     task.pop(Select)
     print(f"Task has been successfully deleted")
   else:
     print(f"Task does not exist")
  except:
   print("Invalid input")

if __name__ == "__main__":
    print("Welcome to Aowi!")
    while True:
        print("\n")
        print("Please select an option from the following")
        print("------------------------------------------")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Display all the tasks")
        print("4. Exit Aowi")
        print("------------------------------------------")
    
        choice= input("Enter your choice: ")
    
        if(choice == "1"):
         addTask()
        elif(choice == "2"):
          DeleteTask()
        elif(choice == "3"):
          DisplayTask()
        elif(choice=="4"):
          break
        else:
          print("Invalid input. Please try again.")
    
    print("Exiting Aowi. Goodbye!")
