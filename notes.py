import os

def addnote():
    f=open("Notes.txt","w")
    ans="y"
    while ans=="y":
        notes=input("Enter your note ")
        ans=input("Do you want to enter more notes?")
        f.write(notes+"\n")
    print("Note added")
    f.close()


def viewnote():
    f=open("Notes.txt","r")
    notes=f.readlines()
    if notes:
            print("\n 📝 Your notes: ")
            for i ,note in enumerate(notes,1):
                print(f"{i}. {note}")
    else:
        print("Notes not found")
    f.close()

def delete_note():
    f=open("Notes.txt","r")
    notes=f.readlines()
    os.remove("Notes.txt")
    print("All notes removed")
   

while True:
    print("\n")
    print("WELCOME TO THE NOTES APP")
    print("1.To add a new note")
    print("2.To view a note")
    print("3.To delete a note")
    print("4.To exit notes app")
    ch=input("Enter the choice you would like to display")
    if ch=="1":
        addnote()
    elif ch=="2":
        viewnote()
    elif ch=="3":
        delete_note()
    elif ch=="4":
        break

    
    
    
