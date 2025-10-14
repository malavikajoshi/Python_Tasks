# 1. Contact List: Create a dictionary to store contacts. Each key should be a name, and the value should be another dictionary with
# phone' and 'email'. Write code to add a new contact and retrieve an existing one.
contacts={}
contacts["karthik"]={"phone":9392461409,"email":"karthikjoshi@gmail.com"}
contacts["malavika"]={"phone":939245345,"email":"malavikajoshi@gmail.com"}
contacts["chandrasekhar"]={"phone":123461409,"email":"chandrasekhar@gmail.com"}
contacts["nagarani"]={"phone":939223459,"email":"nagarani@gmail.com"} 
x=input("want to 'retrieve' or 'enter' data?")
if x=="retrieve":
    print(contacts)
    name=input("enter the name you want the data off:")
    if name in contacts:
        print(contacts[name])
    else:
        print("Data Not Found")
elif x=="enter":
    input_data_name=input("enter your name:")
    input_data_phone=input("enter your phone number:")
    input_data_mail=input("enter your email:")
    contacts[input_data_name]={"phone":input_data_phone,"email":input_data_mail}
    contacts=contacts
    print(contacts)
else:
    print("Good to go....")


# 2. Data Deduplication: Given a list of emails with duplicates, use a set to create a list containing only unique emails. 
l=["malavika@gmail.com","bob@gmail.com","jack@gmail.com","vickyjohn465@gamil.com","nick123@gmail.com","lillymaid@gmail.com","malavika@gmail.com","nick123@gmail.com","vickyjohn465@gamil.com"]
print(set(l))

#3.List Manipulation: Create a to-do list. Write functions to add a task, remove a task by index, and print all tasks.
tasks = ["EAT", "PLAY", "SLEEP", "RUN", "STUDY"]

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added!")

def remove_task(n):
    if 0 <= n < len(tasks):
        removed = tasks.pop(n)
        print(f"Task '{removed}' removed!")
    else:
        print("Invalid index!")

def show_tasks():
    print("Current tasks:")
    for i, task in enumerate(tasks):
        print(i, "-", task)
    print()

show_tasks()
remove_task(2) 
show_tasks()
add_task("EXERCISE")
show_tasks()


    
