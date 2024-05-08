import os

newFile = input("Open new file? (y/n): ")
if newFile == "y":
    #checks if file exists
    if os.path.exists("newFile.txt"):
        #removes file
        os.remove("newFile.txt")
    # opens file with write perms
    f = open("newFile.txt", "w")
    f. write("This is a new file!")
    f.close()

    # opens file that is read-only
    f = open("newFile.txt", "r")
    print(f.read())
    #opens file on desktop
    os.startfile('newFile.txt') 
else:
    print("womp womp")
