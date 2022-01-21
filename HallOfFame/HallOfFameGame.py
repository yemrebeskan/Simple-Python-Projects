def tasklist():     #in there we read file and we created nested list.
    Fileobject = open(r"homework.py\tasklist.txt",encoding = "utf-8")
    task = Fileobject.read().split("\n")
    newlist = []
    for i in task:
        word = i.split(",")
        newlist.append(word)
    return newlist 


def Remove_task(removelist,optiontask):
     #I used recursion for this function,I took two parameter removelist and option 
     # and I removed that option from the list.
    if optiontask.lower() == str(removelist[0]).lower():
        removelist.clear()
    else:
        for lists in removelist:
            #I controlled  element of nested list is list type or not.
            if isinstance(lists,list):
                Remove_task(lists,optiontask)    
    return removelist


def print_remaining_list(printlist,FirstTime = False): 
    #I used recursive function for print new list which I organized
    if len(printlist) > 0 and FirstTime == True:
        print("-" * 40)
        print(printlist)
    for lists in printlist:
        FirstTime = True
        if isinstance(lists,list):
            print_remaining_list(lists,FirstTime)


def optionmenu(tasklist1):
    #in optionmenu I asked whic task user want to go?
    #if option in list I returned option
    while True:
        option = input("Where should Hero go next?")
        for i in (tasklist1):
            if i[0] == option.lower().capitalize():
                return option
        print("Invalid option")        


def vehiclemenu(option,hplist):
    #in there I asked vehicle option
    tasklistv = tasklist()
    condition = True
    while condition:
        vehicle = input("How do you want to travel?(Foot/Pegasus)")
        if vehicle.lower() == "foot":
            for i in tasklistv:
                if i[0] == option.lower().capitalize():
                    #If option is task1 or task2 it will print that and loop will ask vehicle option again.
                    if i[1] == "-1":
                        print("You can not go there by foot.")
                    else:
                        return vehicle
        elif vehicle.lower() == "pegasus":
            for i in range(len(tasklistv)):
                #in there I controlled pegasusHp and if pegasus's hp is not enough for go tasks it will print.
                if tasklistv[i][0] == option.lower().capitalize():
                    if int(tasklistv[i][2]) // 50 * 15 < hplist[1]:
                        return vehicle
                    else:
                        if option.lower().capitalize() == "Task1" or option.lower().capitalize() == "Task2":
                            print("Pegasus does not have enough hp.") 
                            condition = False
                        else:
                            print("Pegasus does not have enough hp.")
        #if vehicle option are not pegasus or foot it will printed                    
        else:
            print("Invalid input.")        
    

def mainmenu():
    print("Welcome to Hero's 5 Labors!")
    tasklist1 = tasklist()
    memorylist = [] #I created memorylist because ı have to take options.
    hplist = [3000,550] #I created hp list.
    #first element of hplist represent heros health second is pegasus hp.
    condition = True #I used that because ı have more than one loop.
    while condition:
        tasklist1.sort() 
        #in there myremovelistfunction return [[],[task1,...],[task2,..]]
        # so ı sorted it and ı provided empty list should be in 0.place
        if tasklist1[0] == []: #I delete my empty list If ı don't do that it will be Index error.
            tasklist1.pop(0)
        if tasklist1 == []:#If list does not has task the user will win the game. 
            Congrulatations(hplist)
            break 
        print(f"Remaining HP for Hero : {hplist[0]}") 
        print(f"Remaining HP for Pegasus : {hplist[1]}\n")
        print("Here are the tasks left that hero needs to complete:")
        print("-" * 60)
        print("|" + " "+ "TaskName"+" " + "|"+ " "+"By FootDistance"+" " + "|" +" " + "By Pegasus"+" "+"|" +"HpNeeded" )
        print_remaining_list(tasklist1) 
        option = optionmenu(tasklist1)      
        vehicle = vehiclemenu(option,hplist)
        #I controlled game over conditions.
        if option.lower().capitalize() == "Task1":
            if hplist[1] < 240: 
                print("GAME OVER")
                condition = False
                continue
        elif option.lower().capitalize() == "Task2":
            if hplist[1] < 150:
                print("GAME OVER")
                condition = False
                continue   
        memorylist.append(option.lower().capitalize()) #I added my tasks (which ı selected) into my memorylist.
        if len(memorylist) > 1: #It should be one element in my memorylist because ı will use it in my home function. 
            memorylist.pop(0) 
        if option.lower() == "task1":
            i = 0
            while i < len(tasklist1):
                if option.capitalize() == tasklist1[i][0]:
                    if hplist[0] >= 50:
                        hplist = task1(hplist,vehicle)
                        tasklist1 = Remove_task(tasklist1,option)#I updated tasklist with using recursion function.
                        break    
                    elif hplist[0] <= 75 or hplist[1] <= 240: #in there I examined game over conditions.
                        print("Game Over") #If it will print game over the condition will be false and loop will be break
                        condition = False
                        break
                i = i + 1             
                if i == len(tasklist1): #in there I checked the list if option is not in list it will print invalid. 
                    print("Invalid input")      
        elif option.lower() == "task2":
            i = 0
            while i < len(tasklist1):#it is like task1.
                if option.capitalize() == tasklist1[i][0]:
                    if hplist[0] > 100:
                        hplist = task2(hplist,vehicle)
                        tasklist1 = Remove_task(tasklist1,option)
                    elif hplist[0] <= 100 or hplist[1] <= 150:
                        print("Game Over")            
                if i == len(tasklist1):
                    print("Invalid input")
                i = i+1    
        elif option.lower() == "task3":
            i = 0
            while i < len(tasklist1): #it is like task1.
                if option.capitalize() == tasklist1[i][0]:
                    if hplist[0] > 75:
                        hplist = task3(hplist,vehicle)
                        tasklist1 = Remove_task(tasklist1,option)
                        break
                    else: 
                        print("Game Over") 
                        condition = False
                        break           
                if i == len(tasklist1):
                    print("Invalid input")
                i = i + 1                   
        elif option.lower() == "task4" :
            i = 0
            while i < len(tasklist1): #it is like task1
                if option.capitalize() == tasklist1[i][0]:
                    if hplist[0] >= 50:
                        hplist = task4(hplist,vehicle)
                        tasklist1 = Remove_task(tasklist1,option) 
                        break
                    else:
                        print("Game Over")
                        condition = False
                        break            
                if i == len(tasklist1):
                    print("Invalid input") 
                i = i + 1     
        elif option.lower() == "task5" : #it is like task1
            i = 0
            while i < len(tasklist1):
                if option.capitalize() == tasklist1[i][0]:
                    if hplist[0] >= 75:
                        hplist = task5(hplist,vehicle)
                        tasklist1 = Remove_task(tasklist1,option)
                        break 
                    else:
                        print("Game Over")
                        condition = False
                        break           
                if i == len(tasklist1):
                    print("Invalid input")
                i = i + 1    
        print(f"Remaining HP for Hero : {hplist[0]}")
        print(f"Remaining HP for Pegasus : {hplist[1]}")             
        hplist = home(hplist,memorylist) #I created home function for come back. 
                  

def task1(hplist,vehicle):
    hplist[0] = hplist[0] - 50 #I computed the remaining heroHp and I updated my list. 50 is the health required to kill monster in task1.
    hour = 400 // 50  #50 is pegasus's velocity,I did not want to use global variable so ı used it like that.
     #15 is that how much pegasus loses hp per a hour.
    hplist[1] = hplist[1] - hour * 15  #I computed the remainingpegasusHP and I updated my list.
    hplist.append(hour)  #I added hours into mylist because ı will compute totalhour in other tasks.
    totalhour = 0
    for i in range(2,len(hplist)): #my hplist's first and second element are remaininghp but other's are hours.
        totalhour = totalhour + hplist[i]
    print("Hero defeated monster")
    print(f"Time passed : {totalhour} hour\n") 
    return hplist #ı will use it in my main program because my program has to write remaining hp every turn.


def task2(hplist,vehicle): #it is like task1 function.
    hplist[0] = hplist[0] - 100 #100 is the health required to kill monster in task2.
    hour = 500 // 50   #50 is pegasus's velocity,I did not want to use global variable so ı used it like that.
    hplist[1] = hplist[1] - hour * 15   #15 is that how much pegasus loses hp per a hour.
    hplist.append(hour)
    totalhour = 0
    for i in range(2,len(hplist)):
        totalhour = totalhour + hplist[i]
    print("Hero defeated monster")
    print(f"Time passed : {totalhour} hour\n")  
    return hplist   


def task3(hplist,vehicle): #it is similar to task1 option but some parts are different.
    hplist[0] = hplist[0] - 75 #75 is the health required to kill monster in task3.
    if vehicle.lower() == "foot":
        hour = 600 // 20 #20 is hero's velocity.
        hplist[0] = hplist[0] - hour * 10 #10 is that how much hero loses hp per a hour.
        hplist.append(hour)
        totalhour = 0
        for i in range(2,len(hplist)):
            totalhour = totalhour + hplist[i]
        print("Hero defeated monster")
        print(f"Time passed : {totalhour} hour\n")    
    elif vehicle.lower() == "pegasus":
        #in task 1 and task2 the only option was pegasus but in task3,task4,task5
        #the user can go to tasks by foot and according to vehicle option ı computed remaining hp.
        hour = 600 // 50 #50 is pegasus's velocity,I did not want to use global variable so ı used it like that.
        hplist[1] = hplist[1] - hour * 15  #15 is that how much pegasus loses hp per a hour.
        hplist.append(hour) 
        totalhour = 0
        for i in range(2,len(hplist)):
            totalhour = totalhour + hplist[i] 
        print("Hero defeated monster")
        print(f"Time passed : {totalhour} hour\n")      
    return hplist     


def task4(hplist,vehicle): #it is like task3.
    hplist[0] = hplist[0] - 50 #50 is the health required to kill monster in task4.
    if vehicle.lower() == "foot":
        hour = 1000 // 20  #20 is hero's velocity.
        hplist[0] = hplist[0] - hour * 10 #10 is that how much hero loses hp per a hour.
        hplist.append(hour)
        totalhour = 0
        for i in range(2,len(hplist)):
            totalhour = totalhour + hplist[i]
        print("Hero defeated monster")
        print(f"Time passed : {hour} hour\n")
       
    elif vehicle.lower() == "pegasus":
        hour = 500 // 50 #50 is pegasus's velocity,I did not want to use global variable so ı used it like that.
        hplist.append(hour)
        totalhour = 0
        for i in range(2,len(hplist)):
            totalhour = totalhour + hplist[i]
        hplist[1] = hplist[1] - hour * 15  #15 is that how much pegasus loses hp per a hour.
        print("Hero defeated monster")
        print(f"Time passed : {totalhour} hour\n")
   
    return hplist     
    


def task5(hplist,vehicle): #it is like task3.
    hplist[0] = hplist[0] - 80 #80 is the health required to kill monster in task5.
    if vehicle.lower() == "foot":
        hour = 900 // 20  #20 is hero's velocity.
        hplist[0] = hplist[0] - hour * 10 #10 is that how much hero loses hp per a hour.
        hplist.append(hour)
        totalhour = 0
        for i in range(2,len(hplist)):
            totalhour = totalhour + hplist[i]
        print("Hero defeated monster")
        print(f"Time passed : {totalhour} hour\n")    
    elif vehicle.lower() == "pegasus":
        hour = 700 // 50 #50 is pegasus's velocity,I did not want to use global variable so ı used it like that.
        hplist[1] = hplist[1] - hour * 15 #15 is that how much pegasus loses hp per a hour.
        hplist.append(hour)
        totalhour = 0
        for i in range(2,len(hplist)):
            totalhour = totalhour + hplist[i]
        print("Hero defeated monster")
        print(f"Time passed : {totalhour} hour\n")      

    return hplist     


def home(hplist,memorylist):
    condition = True
    while condition:
        #ı asked the cohise which is chosen by user.
        choice = input("How do you want to go home?")
        tasklist3 = tasklist()
        string = memorylist[0] 
        #in main program ı created memorylist 
        #I took option which is coming before home part and ı assigned it string.
        for i in tasklist3:
            if string == i[0]:
                if choice.lower() == "foot":
                    if string != "Task1" and string != "Task2":
                        #if that string is not task1 and task2 ı computed herohp.
                        hour = int(i[1]) // 20   #20 is hero's velocity.
                        hplist[0] = int(hplist[0]) - hour * 10 #10 is that how much hero loses hp per a hour.
                        hplist.append(hour)
                        totalhour = 0
                        for i in range(2,len(hplist)):
                            totalhour = totalhour + hplist[i]
                        print("Hero arrived home.")    
                        print(f"Time passed : {totalhour} hour\n")
                        condition = False
                        break
                    else: #if it is task1 or task2 it will be printed.
                        print("You can not go there by foot")        
                elif choice.lower() == "pegasus":
                    #If choise is pegasus ı computed the remaining pegasushp
                    hour = int(i[2]) // 50  #50 is pegasus's velocity,I did not want to use global variable so ı used it like that.
                    hplist[1] = int(hplist[1]) - hour * 15 #15 is that how much pegasus loses hp per a hour.
                    hplist.append(hour)
                    totalhour = 0
                    for i in range(2,len(hplist)): #I computed totalhour ı have to use range(2,len(hplist)) 
                        #because first and second elements are remainingherohp and pegasushp
                        totalhour = totalhour + hplist[i]
                    print("Hero arrived home.")    
                    print(f"Time passed : {totalhour} hour\n")
                    condition = False
                    break
                else:
                    print("Invalid input")            
    return hplist  #ı updated my newhplist   

def Congrulatations(hplist): #if user win the function write user's name and scores
    totalhour = 0
    for i in range(2,len(hplist)):
        totalhour = totalhour + hplist[i] #I computed the score
    print("Congratulations,you have completed the task.")
    name = input("What is your name? ")
    string = name + "," +str(totalhour)+"\n" #I will write it in file so ı assigned my name and score into string.
    writetext(string) 
    PrinterHalloffame()

def writetext(winnerlist):
    #In this function I wrote winners into file.
    FileObject = open(r"homework.py\halloffame","a",encoding="utf-8")
    FileObject.write(winnerlist)   
    FileObject.close()


def readingHalloffame():
    #In there if users
    FileObject = open(r"homework.py\halloffame","r",encoding="utf-8")
    winners = FileObject.read().split("\n")
    winnerlist = []
    winners.pop(-1)
    for i in winners: 
        k = i.split(",")[0]        
        l = i.split(",")[1]
        winnerlist.append([k,l]) #I created new list because ı will sort them
    return winners  


def sortingwinnerlist(): 
    #In there ı sorted my nestedlist according to their elemts's second element.
    winnerlist = readingHalloffame()
    l = len(winnerlist)
    if l > 1:
        for i in range(0,1):
            for j in range(0,l-i-1):
                if winnerlist[j][1] > winnerlist[j+1][1]:
                    tempo = winnerlist[j]
                    winnerlist[j] = winnerlist[j+1]
                    winnerlist[j+1] = tempo
        winnerlist.reverse()            
    return winnerlist 


def PrinterHalloffame(): #it will be printed winners
    sortinglist = sortingwinnerlist()
    print(20 * "-")
    print("|" + "Name" +" " + "|" + "Finish Time"+ "|")
    print(20 * "-")
    if len(sortinglist) >= 3: #if winnerlist's elements bigger than 3 it will be printed the best of 3 user.
        for i in range(3):
           print("|"+ sortinglist[i].split(",")[0]+" "+"|"+sortinglist[i].split(",")[1]+"|")
           print(20 * "-") 
    else:
        for i in range(len(sortinglist)):
            print("|"+ sortinglist[i].split(",")[0]+" "+"|"+sortinglist[i].split(",")[1]+"|")
            print(20 * "-")

mainmenu()


