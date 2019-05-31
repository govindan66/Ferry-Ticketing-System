import datetime
import os
import sys
import random
def clear():            #to make the screen cleared
    os.system('CLS')
    return()
clear()
a=datetime.datetime.now()

print("""
                WELCOME TO FERRY TICKETING SYSTEM

                                                    {}








                                    """.format(a.strftime("Date:%Y-%m-%d| %H:%m")))

print("press Enter to continue....")
input()
clear()

month=a.strftime("%b")
day=a.strftime("%d")
year=a.strftime("%Y")
FID="FID"+"00"+str(random.randint(1,8)) #to generate random ferry ID

seat_Business=[0]*10                #Assigns seat for business class passsenger
seat_Economy=[0]*40                 #Assigns seat for Economy class passengers
class tickets:                      #class to create objects
    def __init__(self,locat,seat,name,age,address,FID,x):
        self.destination=locat
        self.seat=seat
        self.name=name
        self.age=age
        self.address=address
        self.FID=FID
        self.Class= "Business Class" if (x=='1') else "Economy Class"
    def bookTicket(self):           #method to write tickets in a file
        #to save the ticket in the file
        TicketFile=open("ticket.txt","w")   #opens the file in writing mode
        a=datetime.datetime.now()
        b=a.strftime("Date:%Y-%m-%d | %H:%M")   #extracts current time
        TicketFile.write("""
        *********************************************
        *               {}      *
        *********************************************
        {} | Ferry ID:{}
        Seat Number :{}
        Name        :{}
        Age         :{}
        Address     :{}
        Class Type  :{}
        *********************************************""".format(self.destination,b,self.seat,
        self.FID,self.name,self.age,self.address,self.Class))
        TicketFile.close()
        #to get the ticket
    def getTicket(self):
        data=''
        TicketFile=open("ticket.txt","r")
        for x in range(10):
            data=data+TicketFile.readline()
        return(data)
class ViewSeat:                 #class for viewing seat arranement
    def __init__(self):
        self.arrangement="""        ******************************************************
        *               SEATING ARRANGMENT                   *
        ******************************************************
        *  Ferry ID: {}              Date: {} {} {}    *
        ******************************************************
        *  BUSINESS CLASS                                    *
        ******************************************************
        *   {}    *     {}    *     {}     *     {}    *     {}   *
        ******************************************************
        *   {}    *     {}    *     {}     *     {}    *     {}   *
        ******************************************************
        *  ECONOMY CLASS                                     *
        ******************************************************
        *   {}    *     {}    *     {}     *     {}    *     {}   *
        ******************************************************
        *   {}    *     {}    *     {}     *     {}    *     {}   *
        ******************************************************
        *   {}    *     {}    *     {}     *     {}    *     {}   *
        ******************************************************
        *   {}    *     {}    *     {}     *     {}    *     {}   *
        ******************************************************
        *   {}    *     {}    *     {}     *     {}    *     {}   *
        ******************************************************
        *   {}    *     {}    *     {}     *     {}    *     {}   *
        ******************************************************
        *   {}    *     {}    *     {}     *     {}    *     {}   *
        ******************************************************
        *   {}    *     {}    *     {}     *     {}    *     {}   *
        ******************************************************"""
    def viewArrangement(self):
        fileView=open("seat.txt","w")
        fileView.write(self.arrangement.format(FID,day,month,year,*seat_Business,*seat_Economy))
        fileView.close()
    def getArrangement(self):
        fileView=open("seat.txt","r")
        return(fileView.read())
def menu():

    print("""        ******************************************************")
        *                FERRY TICKETING SYSTEM              *
        *                       MAIN MENU                    *
        *         P - to purchase ticket                     *
        *         V - to View seeting arrangement            *
        *         Q - to Quit the system                     *
        ******************************************************""")
    choice=input("Please enter your choice")
    def alert1():
        print("Wrong choice. Kindly choose as specified")
        return menu()
    func_dict={
        'P':purchase,
        "V":view,
        "Q":exit,
        'p':purchase,
        "v":view,
        "q":exit}
    clear()
    func_dict.get(choice,alert1)()

def purchase():
    print("""       **************************************************
        *               PURCHASING MODULE                *
        *                    SUB MENU                    *
        *     B - to purchase ticket for Business class  *
        *     E - to purchase ticket for economy class   *
        *     M - to return to Main Menu                 *
        **************************************************""")
    choice1=input("select your choice")
    def alert2():
        print("Wrong choice. Kindly choose as specified")
        return purchase()
    func_dict1={
    'B':Business,
    "E":Economy,
    "M":menu,
    'b':Business,
    "e":Economy,
    "m":menu}
    clear()
    func_dict1.get(choice1,alert2)()

def view():
    a=ViewSeat()
    a.viewArrangement()
    print(a.getArrangement())
    input("Press Enter to go back to main menu")
    clear()
    return menu()
def Business():
    for x in seat_Business:
        if x==0:
            break   #to ensure if the business class seat is vacant
    else:
        print("Sorry! the business class seat is full")
        print("do you want to book economy class?")
        alter=input("enter Y or N")
        if alter=="Y" or alter=="y":
            Economy()
            return
        elif alter=="N" or alter=="n":
            print("Next trip leaves in next one hour.")
            return
        else:
            clear()
            print ("You entered wrong choice. Please try again")
            return Business()
    try:
        SeatNo=int(input("please enter your desired seat number"))

    except:
        print("Please enter a number between 1 and 10")
        return Business()
    if SeatNo>10 or SeatNo<1:
        print("Please choose between 1 to 10")
        return Business()
    elif seat_Business[SeatNo-1]==0:
        seat_Business[SeatNo-1]=1
    else:
        print("sorry! the seat is already reserved. Choose another seat number")
        return Business()
    SeatReserve(SeatNo,1)

    return menu()
def SeatReserve(SeatNo,x):  #function to get the deatil of the passenger
    try:
        age=int(input("Enter your age"))
    except:
        print("Enter your age in numbers")
        return SeatReserve(SeatNo,x)
    print("Enter your destination\n1.Penang to Langkawi\n2.Langkawi to Penang")
    location=int(input("Enter 1 or 2"))
    if location==1:
        Loc="PENANG TO LANGKAWI"
    else:
        Loc="LANGKAWI TO PENANG"
    name=input("Enter your name")
    address=input("Enter your address")
    myTicket=tickets(Loc,SeatNo,name,age,address,FID,x)
    myTicket.bookTicket()
    clear()
    print("You have successfully purchased ticket.\n")
    input("press enter to view your ticket")
    clear()
    print(myTicket.getTicket())
    input("Press enter to return to Main menu")

def Economy():
    for x in seat_Economy:
        if x==0:
            break   #to ensure if the economy class seat is vacant
    else:
        print("Sorry! this deck is completely full")
        if 0 in seat_Business:
            print("Do you like to book business class ticket?(Y/N)")
            alter=input("Enter either Y or N")
            if alter=='Y' or alter=='y':
                return Business()
            else:
                print("Please wait till the next trip?")
    try:
        SeatNo=int(input("please enter your desired seat number"))
    except:
        print("Please enter a number between 11 and 50")
    if SeatNo>50 or SeatNo<11:
        print("Please choose between 11 to 50")
        return Economy()
    elif seat_Economy[SeatNo-11]==0:
        seat_Economy[SeatNo-11]=1
    else:
        print("sorry! the seat is already reserved. Choose another seat number")
        return Economy()
    SeatReserve(SeatNo,0)
    clear()
    return menu()
menu()



