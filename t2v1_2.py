from Tkinter import *
import datetime as dt
from random import sample
import random
import numpy as np
import array as arr

frmt = '%H:%M:%S'
trainFrmt = '%d-%m-%Y %H:%M'

TotalDuration = 60
Iterations = 5
waitAtEndStop = 15
TrainEvery_min = 30


startTimefromA = dt.datetime(2018,10,27,10,00,00,00)
startTime = startTimefromA
endTime = startTime + dt.timedelta(minutes=TotalDuration)
nextTrain = endTime + dt.timedelta(minutes=waitAtEndStop)

beforeTrain = startTime - dt.timedelta(minutes=TotalDuration - waitAtEndStop)
time_elapsed=nextTrain - beforeTrain
numOfTrains = int(time_elapsed.total_seconds()/(TrainEvery_min*60))




startTimefromB = startTimefromA - dt.timedelta( minutes=45)
trainsToB=[]
trainsToA=[]
trainsToBstring=[]
trainsToAstring=[]



def TrainTimetables(numOfStations):
    

    for i in xrange(Iterations):
        global startTimefromA
        global startTimefromB
        trainsToB.append([])
        trainsToBstring.append([])
        trainsToA.append([])
        trainsToAstring.append([])
        temp = startTimefromA
        temp2 = startTimefromB
        for j in xrange(numOfStations):
            trainsToB[i].append(startTimefromA)
            trainsToA[i].append(startTimefromB)
            trainsToBstring[i].append(dt.datetime.strftime(startTimefromA, frmt))
            trainsToAstring[i].append(dt.datetime.strftime(startTimefromB, frmt))
            startTimefromA+=dt.timedelta(minutes=TotalDuration/float(numOfStations-1))
            startTimefromB+=dt.timedelta(minutes=TotalDuration/float(numOfStations-1))
        startTimefromA=temp+dt.timedelta(minutes=TrainEvery_min)
        startTimefromB=temp2+dt.timedelta(minutes=TrainEvery_min)

# TrainTimetables(10)

    print np.matrix(trainsToBstring)
    print "\n"
    print np.matrix(trainsToAstring)

        


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end


def main(numOfStations):
    # Users = int(E1.get())
    countA=0
    countB=0
    trainTimeUser=[]
    global trainsToA
    global trainsToB
    Users=30
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
    UsersTowardsB=[]
    UsersTowardsA=[]
    trainTimeUserString=[]

    UsersStationsFromA = []
    UsersStationsFromB = []

    for i in xrange(numOfStations):
        UsersStationsFromA.append(0)
        UsersStationsFromB.append(0)

    for i in xrange(Users):
        cabsTowardStation.append(0)
        cabsTowardDestination.append(0)

    Atime, Btime, AtimeString, DtimeString = ([] for i in range(4)) 

    List_of_Lists = [UsersList,  UsersStartStation,  UsersDestinationStation, cabsTowardStation,  AtimeString, trainTimeUserString, DtimeString, totalTime]

    for i in range(Users): #Users List
        UsersList.append("User "+str(i+1))

    
    TrainTimetables(numOfStations)

    i=0


    # Time slot allotments --  -- this is where the magic happens -- -
    while i < Users:
        j=i 

        UsersDtemp = random.randint(1, numOfStations-1)
        UsersAtemp = random.randint(0,numOfStations-2)

        if UsersAtemp == UsersDtemp:
            i=j
            continue
        else:
            UsersDestinationStation.append(UsersDtemp)
            UsersStartStation.append(UsersAtemp)



        if UsersStartStation[i] < UsersDestinationStation[i]:
            UsersStationsFromA[UsersAtemp] = int(float(UsersStationsFromA[UsersAtemp])+1)
            countA+=1
            stationGaps = UsersDestinationStation[i]- UsersStartStation[i]

            tempA = random.randint(0, Iterations-1)

            trainTimeUser.append(trainsToB[tempA][UsersStartStation[i]])
    
            Atime.append(sample([ trainTimeUser[i] - dt.timedelta(minutes = x, seconds = y) for x in range(3, 29) for y in range(0, 60) ], 1))
            Btime.append(sample([ trainTimeUser[i]+ dt.timedelta(minutes=(TotalDuration/float(numOfStations))*stationGaps) + dt.timedelta(minutes = x, seconds = y) for x in range(3, 29) for y in range(0, 60) ], 1))

        # elif UsersStartStation[i] == UsersDestinationStation[i]:
        #     a=1

        else:
            UsersStationsFromB[(numOfStations) - UsersStartStation[i]-1] = int(float(UsersStationsFromB[(numOfStations) - UsersStartStation[i]-1]) + 1)
            countB+=1
            stationGaps = UsersStartStation[i] - UsersDestinationStation[i]

            temp = random.randint(0, Iterations-1)

            trainTimeUser.append(trainsToA[temp][(numOfStations) - UsersStartStation[i]-1])
    
            Atime.append(sample([ trainTimeUser[i] - dt.timedelta(minutes = x, seconds = y) for x in range(3, 29) for y in range(0, 60) ], 1))
            Btime.append(sample([ trainTimeUser[i] + dt.timedelta(minutes=(TotalDuration/float(numOfStations))*stationGaps) + dt.timedelta(minutes = x, seconds = y) for x in range(3, 29) for y in range(0, 60) ], 1))

        i += 1
    



    for sublist in Atime:
        for item in sublist:
            flat_list_A.append(item)

    for sublist in Btime:
        for item in sublist:
            flat_list_D.append(item)


 

    for i in range(Users):
        td = (flat_list_D[i] - flat_list_A[i])
        hours, minutes = td.seconds // 3600, td.seconds // 60 % 60
        totalTime.append(str(hours)+" Hr "+str(minutes)+" min ")
        AtimeString.append(dt.datetime.strftime(flat_list_A[i], frmt))
        DtimeString.append(dt.datetime.strftime(flat_list_D[i], frmt))
        trainTimeUserString.append(dt.datetime.strftime(trainTimeUser[i], frmt))
    
    c=0

    for i in xrange(Users):
        cabNo=random.randint(1,Users/3)
        print cabNo
        j+=1
        for j in xrange(Users):
            if trainTimeUserString[j]==trainTimeUserString[i]:
                cabsTowardStation[i]=="Cab No."+str(cabNo)+" to station-"+str(UsersStartStation[i])
                cabsTowardStation[j]=="Cab No."+str(cabNo)+" to station-"+str(UsersStartStation[j])
                c+=1

    print str(c)+" this" 
           
            
    
    for i in xrange(Users):
        if cabsTowardStation[i]==0:
            cabsTowardStation.append("Cab No."+str(random.randint(1,Users))+" to station-"+str(UsersStartStation[i]))
        
        
        
    



  


    # print UsersFromA
    # for i in range(Users): #Users start stations and Cabs Allotment towards station
    #     if UsersStartStation[i] == 0:
    #         cabsTowardStation.append("Cab No."+str(random.randint(1, (UsersFromA/3)+1))+" to A")
    #         UsersStartStationLetter.append("A")
    #     elif UsersStartStation[i] == 1:
    #         cabsTowardStation.append("Cab No."+str(random.randint(1, (UsersFromB/3)+1))+" to B")
    #         UsersStartStationLetter.append("B")
    #     elif UsersStartStation[i] == 2:
    #         cabsTowardStation.append("Cab No."+str(random.randint(1, (UsersFromC/3)+1))+" to C")
    #         UsersStartStationLetter.append("C")
    #     else:
    #         cabsTowardStation.append("Cab No."+str(random.randint(1, (UsersFromD/3)+1))+" to D")
    #         UsersStartStationLetter.append("D")

    # for i in range(Users): #Users end station and Cabs Allotment towards destinations
    #     if UsersDestinationStation[i] == 1:
    #         cabsTowardDestination.append("Cab No."+str(random.randint(1, (UsersToB/3)+1))+"i From B")
    #         UsersDestinationStationLetter.append("B")
    #     elif UsersDestinationStation[i] == 2:
    #         cabsTowardDestination.append("Cab No."+str(random.randint(1, (UsersToC/3)+1))+"i From C")
    #         UsersDestinationStationLetter.append("C")
    #     elif UsersDestinationStation[i] == 3:
    #         cabsTowardDestination.append("Cab No."+str(random.randint(1, (UsersToD/3)+1))+"i From D")
    #         UsersDestinationStationLetter.append("D")
    #     else:
    #         cabsTowardDestination.append("Cab No."+str(random.randint(1, (UsersToE/3)+1))+"i From E")
    #         UsersDestinationStationLetter.append("E")


    # print "Train from Station A --  -- " + dt.datetime.strftime(AtrainTime, trainFrmt)
    # print "Train from Station B --  -- " + dt.datetime.strftime(BtrainTime, trainFrmt)
    # print "Train from Station C --  -- " + dt.datetime.strftime(CtrainTime, trainFrmt)
    # print "Train from Station D --  -- " + dt.datetime.strftime(DtrainTime, trainFrmt)
    # print "Train from Station E --  -- " + dt.datetime.strftime(EtrainTime, trainFrmt)




    
#     trainstationlist = ['A', 'B', 'C', 'D', 'E']
#     trainTimeList = [AtrainTime, BtrainTime, CtrainTime, DtrainTime, EtrainTime]
#     genderList = ['his', 'her']

#     ListFrame = Frame(window)
#     ListFrame.pack(side = BOTTOM)
#     ListFrame.destroy()
#     # for frame in ListFrame.

#     # scrollbar = Scrollbar(window) 
#     # scrollbar.pack( side = RIGHT)
#     Lb = Listbox(window, bg='green', height=5, width=22)

#     for i in xrange(len(trainstationlist)):
#         Lb.insert(END, 'Train from '+trainstationlist[i]+' at '+ dt.datetime.strftime(trainTimeList[i], trainFrmt))

#     Lb.pack(anchor = CENTER)

#     Lb1 = Listbox(window, height=Users)
#     for i in range(Users):
#         Gender = genderList[random.randint(0, 1)]

#         Lb1.insert(END, UsersList[i]+' will start '+Gender+' journey at '+AtimeString[i]+ ' will take '+cabsTowardStation[i]+' and reach '+Gender+' destination at '+DtimeString[i]+ ' by taking '+cabsTowardDestination[i]+'. Total Time taken = '+totalTime[i])
#     Lb1.pack(fill = BOTH)
#     # scrollbar.config( command = Lb.yview )


    # print "\n\n" 
    for a in zip(*List_of_Lists):
        print a

    print countA, countB
    print numOfTrains
    print UsersStationsFromA
    print UsersStationsFromB
  

if __name__ == '__main__':
    main(10)
    
 
# # Users = input("Enter no of Users: ")
# window = Tk()
# window.title("BTP-Feeder")
# window.geometry("500x500")

# label = Label( text = "Enter no of Users", pady = 3 )

# label.config(font = ("Times New Roman", 22))
# label.pack()
# E1 = Entry( bd = 3)
# E1.pack()

# button1 = Button(text = "Submit", bg = "red", font = ("Times New Roman", 15), command = lambda : main())
# button1.pack()





   










# window.mainloop()   

