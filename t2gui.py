from Tkinter import *
import datetime as dt
from random import sample
import random

frmt = '%H:%M:%S'
trainFrmt = '%d-%m-%Y %H:%M'

    
def main():
    Users = int(E1.get())
    UsersList = []
    UserStartTime = []
    UserStartTimeString = []
    UsersStartStation = []
    UsersStartStationLetter = []
    UsersDestinationStationLetter = []
    UsersDestinationStation = []
    flat_list_A = []
    flat_list_D = []
    totalTime = []
    cabsTowardStation = []
    cabsTowardDestination = []
    UsersFromA = 0
    UsersFromB = 0
    UsersFromC = 0
    UsersFromD = 0
    UsersToB = 0
    UsersToC = 0
    UsersToD = 0
    UsersToE = 0


    Atime, Dtime, AtimeString, DtimeString = ([] for i in range(4)) 

    List_of_Lists = [UsersList,  UsersStartStationLetter,  UsersDestinationStationLetter, cabsTowardStation, AtimeString, DtimeString, cabsTowardDestination, totalTime]

    for i in range(Users):
        UsersList.append("User "+str(i+1))

    sample_date = dt.datetime.now()+dt.timedelta(minutes = 45)

    AtrainTime = sample_date
    BtrainTime = AtrainTime + dt.timedelta(minutes = 30)
    CtrainTime = BtrainTime + dt.timedelta(minutes = 30) 
    DtrainTime = CtrainTime + dt.timedelta(minutes = 30)
    EtrainTime = DtrainTime + dt.timedelta(minutes = 30)



    # print UsersDestinationStation
    # print UsersStartStation

    # Time slot allotments --  -- this is where the magic happens -- -
    for i in range(Users): 
        UsersDestinationStation.append(random.randint(1, 4))
        UsersStartStation.append(random.randint(0, UsersDestinationStation[i]-1))

        if UsersDestinationStation[i] == 1:
            UsersToB += 1
            UsersFromA += 1
            Atime.append(sample([sample_date - dt.timedelta(minutes = x, seconds = y) for x in range(3, 35) for y in range(0, 60)], 1))
            Dtime.append(sample([BtrainTime + dt.timedelta(minutes = x, seconds = y) for x in range(1, 28) for y in range(0, 60)], 1))
        
        elif UsersDestinationStation[i] == 2:
            UsersToC += 1
            if UsersStartStation[i] == 0:
                UsersFromA += 1
                Atime.append(sample([sample_date - dt.timedelta(minutes = x, seconds = y) for x in range(3, 35) for y in range(0, 60)], 1))
                Dtime.append(sample([CtrainTime + dt.timedelta(minutes = x, seconds = y) for x in range(1, 28) for y in range(0, 60)], 1))
            else:
                UsersFromB += 1
                Atime.append(sample([BtrainTime - dt.timedelta(minutes = x, seconds = y) for x in range(3, 28) for y in range(0, 60)], 1))
                Dtime.append(sample([CtrainTime + dt.timedelta(minutes = x, seconds = y) for x in range(1, 28) for y in range(0, 60)], 1))
    
        elif UsersDestinationStation[i] == 3:
            UsersToD += 1
            if UsersStartStation[i] == 0:
                UsersFromA += 1
                Atime.append(sample([sample_date - dt.timedelta(minutes = x, seconds = y) for x in range(3, 35) for y in range(0, 60)], 1))
                Dtime.append(sample([DtrainTime + dt.timedelta(minutes = x, seconds = y) for x in range(1, 28) for y in range(0, 60)], 1))
            elif UsersStartStation[i] == 1:
                UsersFromB += 1
                Atime.append(sample([BtrainTime - dt.timedelta(minutes = x, seconds = y) for x in range(3, 28) for y in range(0, 60)], 1))
                Dtime.append(sample([DtrainTime + dt.timedelta(minutes = x, seconds = y) for x in range(1, 28) for y in range(0, 60)], 1))
            else:
                UsersFromC += 1
                Atime.append(sample([CtrainTime - dt.timedelta(minutes = x, seconds = y) for x in range(3, 28) for y in range(0, 60)], 1))
                Dtime.append(sample([DtrainTime + dt.timedelta(minutes = x, seconds = y) for x in range(1, 28) for y in range(0, 60)], 1))
        
        else:
            UsersToE += 1
            if UsersStartStation[i] == 0:
                UsersFromA += 1
                Atime.append(sample([sample_date - dt.timedelta(minutes = x, seconds = y) for x in range(3, 35) for y in range(0, 60)], 1))
                Dtime.append(sample([EtrainTime + dt.timedelta(minutes = x, seconds = y) for x in range(1, 28) for y in range(0, 60)], 1))
            elif UsersStartStation[i] == 1:
                UsersFromB += 1
                Atime.append(sample([BtrainTime - dt.timedelta(minutes = x, seconds = y) for x in range(3, 28) for y in range(0, 60)], 1))
                Dtime.append(sample([EtrainTime + dt.timedelta(minutes = x, seconds = y) for x in range(1, 28) for y in range(0, 60)], 1))
            elif UsersStartStation[i] == 2:
                UsersFromC += 1
                Atime.append(sample([CtrainTime - dt.timedelta(minutes = x, seconds = y) for x in range(3, 28) for y in range(0, 60)], 1))
                Dtime.append(sample([EtrainTime + dt.timedelta(minutes = x, seconds = y) for x in range(1, 28) for y in range(0, 60)], 1))
            else:
                UsersFromD += 1
                Atime.append(sample([DtrainTime - dt.timedelta(minutes = x, seconds = y) for x in range(3, 28) for y in range(0, 60)], 1))
                Dtime.append(sample([EtrainTime + dt.timedelta(minutes = x, seconds = y) for x in range(1, 28) for y in range(0, 60)], 1))




    for sublist in Atime:
        for item in sublist:
            flat_list_A.append(item)

    for sublist in Dtime:
        for item in sublist:
            flat_list_D.append(item)


    # print flat_list_A
    # print "\n\n" 
    # print flat_list_D

    for i in range(Users):
        td = (flat_list_D[i] - flat_list_A[i])
        hours, minutes = td.seconds // 3600, td.seconds // 60 % 60
        totalTime.append(str(hours)+" Hr "+str(minutes)+" min ")
        AtimeString.append(dt.datetime.strftime(flat_list_A[i], frmt))
        DtimeString.append(dt.datetime.strftime(flat_list_D[i], frmt))


    # print UsersFromA
    for i in range(Users): #Users start stations and Cabs Allotment towards station
        if UsersStartStation[i] == 0:
            cabsTowardStation.append("Cab No."+str(random.randint(1, (UsersFromA/3)+1))+" to A")
            UsersStartStationLetter.append("A")
        elif UsersStartStation[i] == 1:
            cabsTowardStation.append("Cab No."+str(random.randint(1, (UsersFromB/3)+1))+" to B")
            UsersStartStationLetter.append("B")
        elif UsersStartStation[i] == 2:
            cabsTowardStation.append("Cab No."+str(random.randint(1, (UsersFromC/3)+1))+" to C")
            UsersStartStationLetter.append("C")
        else:
            cabsTowardStation.append("Cab No."+str(random.randint(1, (UsersFromD/3)+1))+" to D")
            UsersStartStationLetter.append("D")

    for i in range(Users): #Users end station and Cabs Allotment towards destinations
        if UsersDestinationStation[i] == 1:
            cabsTowardDestination.append("Cab No."+str(random.randint(1, (UsersToB/3)+1))+"i From B")
            UsersDestinationStationLetter.append("B")
        elif UsersDestinationStation[i] == 2:
            cabsTowardDestination.append("Cab No."+str(random.randint(1, (UsersToC/3)+1))+"i From C")
            UsersDestinationStationLetter.append("C")
        elif UsersDestinationStation[i] == 3:
            cabsTowardDestination.append("Cab No."+str(random.randint(1, (UsersToD/3)+1))+"i From D")
            UsersDestinationStationLetter.append("D")
        else:
            cabsTowardDestination.append("Cab No."+str(random.randint(1, (UsersToE/3)+1))+"i From E")
            UsersDestinationStationLetter.append("E")


    print "Train from Station A --  -- " + dt.datetime.strftime(AtrainTime, trainFrmt)
    print "Train from Station B --  -- " + dt.datetime.strftime(BtrainTime, trainFrmt)
    print "Train from Station C --  -- " + dt.datetime.strftime(CtrainTime, trainFrmt)
    print "Train from Station D --  -- " + dt.datetime.strftime(DtrainTime, trainFrmt)
    print "Train from Station E --  -- " + dt.datetime.strftime(EtrainTime, trainFrmt)
    
    trainstationlist = ['A', 'B', 'C', 'D', 'E']
    trainTimeList = [AtrainTime, BtrainTime, CtrainTime, DtrainTime, EtrainTime]
    genderList = ['his', 'her']

    ListFrame = Frame(window)
    ListFrame.pack(side = BOTTOM)
    ListFrame.destroy()
    # for frame in ListFrame.

    # scrollbar = Scrollbar(window) 
    # scrollbar.pack( side = RIGHT)
    Lb = Listbox(window, bg='green', height=5, width=22)

    for i in xrange(len(trainstationlist)):
        Lb.insert(END, 'Train from '+trainstationlist[i]+' at '+ dt.datetime.strftime(trainTimeList[i], trainFrmt))

    Lb.pack(anchor = CENTER)

    Lb1 = Listbox(window, height=Users)
    for i in range(Users):
        Gender = genderList[random.randint(0, 1)]

        Lb1.insert(END, UsersList[i]+' will start '+Gender+' journey at '+AtimeString[i]+ ' will take '+cabsTowardStation[i]+' and reach '+Gender+' destination at '+DtimeString[i]+ ' by taking '+cabsTowardDestination[i]+'. Total Time taken = '+totalTime[i])
    Lb1.pack(fill = BOTH)
    # scrollbar.config( command = Lb.yview )


    print "\n\n" 
    for a in zip(*List_of_Lists):
        print a


 
# Users = input("Enter no of Users: ")
window = Tk()
window.title("BTP-Feeder")
window.geometry("500x500")

label = Label( text = "Enter no of Users", pady = 3 )

label.config(font = ("Times New Roman", 22))
label.pack()
E1 = Entry( bd = 3)
E1.pack()

button1 = Button(text = "Submit", bg = "red", font = ("Times New Roman", 15), command = lambda : main())
button1.pack()



   










window.mainloop()   

