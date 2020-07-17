#PF-Assgn-55

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name):
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[2].startswith(destination)):
            count+=1
    return count
   

def find_passengers_per_flight():
    flight=[]
   
    for string in ticket_list:
        count=0
        string_list=string.split(":")
        str1=""
        if string_list[0] not in flight: 
            flight.append(string_list[0])
        
    for i in range(0,len(flight)):
        count=0
        count=find_passengers_flight(flight[i])
        flight[i]=flight[i]+":"+str(count)
    
    return flight     
        
    
def sort_passenger_list():
    unsorted=find_passengers_per_flight()
    temp1=[]
    for i in unsorted:
        temp=i.split(":")
        temp1.append(temp[1])
    temp1.sort(reverse=True)
    
    for i in temp1:
        index=temp1.index(i)
        for num in unsorted:
            t=num.split(":")
            if(i==t[1]):
                temp1[index]=t[0]+":"+i
            else:
                continue
    return temp1

print(find_passengers_flight("BA"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())