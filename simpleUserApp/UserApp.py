def displaymenu():
    print("1. Log in / change user")
    print("2. Create new user")
    print("3. Add friend")
    print("4. Show my friends")
    print("5. Exit")


def menuloop():
    while True:
        displaymenu()
        option = input()
        if option.isdigit() and 1 <= int(option) <= 5:
            break
        else:
            print("Invalid option\n")
    return option  


def MainMenu():
    username = ""
    while True:
        option = menuloop()
        if option == "1":
            if username != "":
                username = ""
                username = login()
            else:    
                username = login()
        elif option == "2":
            createNewUser()
        elif option == "3":
            if username == "":
                print("You need to log in first\n")
                continue
            else:
                Addnewfriend(username)
        elif option == "4":
            if username == "":
                print("You need to log in first\n")
                continue
            else:
                Showmyfriends(username)
        elif option == "5":
            break    


def createlist():  
    Fileobject = open("users.txt",encoding="utf-8")
    users = Fileobject.readlines()
    return users   


def createdict():
    userdict = dict()
    Fileobject = open("users.txt",encoding="utf-8")
    users = Fileobject.readlines()
    for i in users:
        name,password,friendss = i.split(";")
        friends = friendss.split("\n")[0]
        userdict[name] = (password,friends)
    return userdict



def login():
    userdict = createdict()
    username = input("Please enter username:\n")
    password = input("Please enter password:\n")
    if username in userdict.keys() and password == userdict[username][0]:
        print("Logged in\n")
        return username
    else:
        print("Wrong password or username\n")   



def validateusername(username):
    string = "abcçdefgğhıijklmnoöprsştuüvyz0123456789"
    userdict = createdict()
    if username in userdict.keys():
        return False
    for i in username:
        if i not in string or i == " ":
            return False
    return True             



def validatepassword(password): 
    string = "AaBbCcÇçDdEeFfGgğHhIıİiJjKkLlMmNnOoÖöPpRrSsŞşTtUuÜüVvYyZz0123456789"
    if len(password) < 4 and len(password) > 8:
        return False
    for char in password:
        if char not in string:
            return False
    return True           



def createNewUser():
    username = input("Please enter username:\n")
    password = input("Please enter password:\n")
    if validateusername(username):
        if validatepassword(password):
            userlist = createlist()
            userlist.append(f"{username};{password};\n") 
            Fileobject = open("users.txt","w",encoding="utf-8") 
            for user in userlist:
                Fileobject.write(user)   
            Fileobject.close()    
        else:
            print("Password not valid.\n")   
    else:
        print("Username not valid.\n")



def Addnewfriend(username):
    userlist = createlist()
    list1,list2,list3 = [],[],[]
    for i in userlist:
        user,password,friend = i.split(";")
        list1.append(user)
        list2.append(password)
        list3.append(friend)
    list4 = []    
    for i in list3:
        list4.append(i.split("\n")[0])    
    friend = input("Please enter the name of your new friend:\n")
    if friend in list1:
        list4[list1.index(username)] = list4[list1.index(username)] + "," + friend 
        list5 = []    
        for i in list4:
            list5.append(i + "\n")
        list6 = []
        for i in range(len(list1)):
            list6.append(list1[i] + ";" + list2[i] + ";" + list5[i])  
        Fileobject = open("users.txt","w",encoding = "utf-8")
        for friends in list6:
            Fileobject.write(friends) 
        Fileobject.close()       
    else:
        print("Friend not found\n") 

        
                 
def Showmyfriends(username):
    userdict = createdict()
    print(userdict[username][1])
MainMenu()