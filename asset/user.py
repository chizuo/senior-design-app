import uuid
import os.path
from os import path

class AppHash:
    def __init__(self) -> None:
        if(path.exists('./config/user.txt')):
            userFile = open('./config/user.txt','r')
            self.hashedID = userFile.read()
            print(self.hashedID)
        else:
            userFile = open('./config/user.txt','a')
            self.hashedID = hex(uuid.getnode())
            userFile.write(self.hashedID)







