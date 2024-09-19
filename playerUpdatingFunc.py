#Using RegEx (Regular expressions) and OOP (classes)

import os
import re
user_dict = {}

class PlayerInfo:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password

    def savePlayerInfo(self):
        if not os.path.exists("./playerInfo.txt"):
            with open("playerInfo.txt", "x") as file:
                pass
        else:
            pass
        with open("playerInfo.txt", "r") as file:
            for line in file.readlines():
                pattern = r"(\w+)\s*:\s*(\w+)" # (\w+) isfor word char classes at one or more occurences, s* is for whitespaces any any occurences, each class in () is stored under a group in the regex starting with 1
                findUser = re.match(pattern, line) # find all matches that match the pattern in line
                if findUser:
                    user = findUser.group(1)  # Extract the username (group 1 from the regex)
                    if self.username == user:
                        print("Username already exists!")
                        return
                else:
                    pass

        with open("playerInfo.txt", "a") as file:
            file.write(f"{self.username}: {self.password}\n")


username = input("Enter a valid username: ")
password = input("Enter a password: ")

playerUpdate = PlayerInfo(username, password)
playerUpdate.savePlayerInfo()

with open("playerInfo.txt", "r") as file:
    for line in file.readlines():
        user, pword = line.strip().split(': ')
        user_dict[user.strip()] = pword.strip()

print(user_dict)
