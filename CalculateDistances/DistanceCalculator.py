Filemember = open("provinces.txt",encoding="utf-8")
lines = Filemember.readlines()
lines.sort()
citydict = dict()
for i in lines:
    city,xcordinate,ycordinate = i.split(",")
    citydict[city] = (xcordinate,ycordinate)
login = True
longcities1 = []
longcities2 = []
while login:
    string1 = ""
    departure = input("Departure province:\n")
    if departure.upper() not in citydict.keys():
        print("Province not found!")
        for i in citydict.keys():
            if departure.upper() in i[0:len(departure)]:
                string1 = string1 + i + ","
                longcities1.append(i)
        string1 = string1[0:-1]       
        if len(string1) != 0:
            if len(longcities1) > 1:
                print(f"Possible provinces:{string1}")
            elif len(longcities1) == 1:
                print(f"Possible province:{string1}")    
            continue
        continue
    cont = True         
    while cont:       
        string2 = ""
        arrival = input("Arrival province:\n")
        if arrival.upper() in citydict.keys() and arrival.upper() != departure.upper():
            cont = False
        elif  arrival.upper() == departure.upper():  
            print("Enter a different province!")
        elif arrival.upper() not in citydict.keys(): 
            print("Province not found!")  
            for i in citydict.keys():
                if arrival.upper() in i[0:len(arrival)]:
                    string2 = string2 + i + ","
                    longcities2.append(i)
            string2 = string2[0:-1]
            if len(string2) != 0:
                if len(longcities2) > 1:
                    print(f"Possible provinces:{string2}")
                elif len(longcities2) == 1:
                    print(f"Possible province:{string2}")            
    else:
        login = False 
x1 = citydict[departure.upper()][0]
y1 = citydict[departure.upper()][1]
x2 = citydict[arrival.upper()][0]
y2 = citydict[arrival.upper()][1]
x1,y1,x2,y2 = float(x1),float(y1),float(x2),float(y2)
dx = x2 - x1
dy = y2 - y1
distance = (dx * dx + dy * dy) ** 0.5
distancekm = distance * 100
distancekm = round(distancekm,2)
vcar = 90
vmotorcycle = 80
vbicycle = 25
while True:
    vehicle = input("Enter travel type:\n")
    if vehicle.upper() == "CAR":
        time = distancekm / vcar
        break
    elif vehicle.upper() == "MOTORCYCLE":
        time = distancekm / vmotorcycle
        break
    elif vehicle.upper() == "BICYCLE":
        time = distancekm / vbicycle
        break
hour = int(time)
minute = (time - hour) * 60   
minute = int(minute)
print(f"\nI am calculating the distance between {departure.upper()} and {arrival.upper()} ...\n")
print(f"Distance: {distancekm} km") 
print(f"Approximate travel time with {vehicle.upper()}: {hour} hours {minute} minutes")  
listcity = []
listdistance = []
listcity.extend(citydict.keys())
listcity.remove(departure.upper())
index = 3
string5 = ""
for i in listcity:
        y4 = citydict[i][1]
        x4 = citydict[i][0]
        y4,x4 = float(y4),float(x4)
        dy2 = y4 - y1
        dx2 = x4 - x1
        distance2 = (dy2 * dy2 + dx2 * dx2) ** 0.5
        distance2km = distance2 * 100
        listdistance.append(distance2km)
while index != 0:
    mindistance = 100000000
    for i in range(len(listdistance)):
        if listdistance[i] < mindistance:
            mindistance = listdistance[i]
    string5 = string5 + listcity[listdistance.index(mindistance)] + ","
    listcity.pop(listdistance.index(mindistance))
    listdistance.remove(mindistance)  
    index = index - 1   
string5 = string5[0:-1]
cities = string5.split(",")    
cities.sort()
string6 = ""
for i in cities:
    string6 = string6 + i + ","
string6 = string6[0:-1]    
print(f"Recommended places close to {departure.upper()}:{string6}")
                 
       


    




                

               














      
    









    


    
    








    

    
           
                  





    








    
            


               


                     


        
          
                      

 

 


   
  


