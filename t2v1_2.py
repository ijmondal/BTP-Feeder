from Tkinter import *
import datetime as dt
from random import sample
import random
import numpy as np
from collections import Counter

frmt = '%H:%M:%S'
trainFrmt = '%d-%m-%Y %H:%M'

# TotalDuration = 60
# Iterations = 5
# waitAtEndStop = 15
# TrainEvery_min = 30


startTimefromA = dt.datetime(2018,10,27,10,00,00,00)

trainsToB=[]
trainsToA=[]
trainsToBstring=[]
trainsToAstring=[]



def TrainTimetables(Users, TotalDuration, numOfStations, Iterations, TrainEvery_min, waitAtEndStop):
    global startTimefromA
    startTime = startTimefromA
    endTime = startTime + dt.timedelta(minutes=TotalDuration)
    nextTrain = endTime + dt.timedelta(minutes=waitAtEndStop)

    beforeTrain = startTime - dt.timedelta(minutes=TotalDuration - waitAtEndStop)
    time_elapsed=nextTrain - beforeTrain
    numOfTrains = int(time_elapsed.total_seconds()/(TrainEvery_min*60))

    startTimefromB = beforeTrain
    

    for i in xrange(Iterations):
       
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
    print "\n"
    print "##########################Train Timinigs towards B #######################"
    for row in trainsToBstring:
        print row
    print "\n"
    print "##########################Train Timinigs towards A #######################"
    for row in trainsToAstring:
        print row

    return numOfTrains

        


def time_in_range(start, end, x):
    """Return true if x is in the range [start, end]"""
    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end

def duplicates(lst, item):
    return [i for i, x in enumerate(lst) if x == item]


def main(Users, TotalDuration, numOfStations, Iterations, TrainEvery_min, waitAtEndStop ):
    # Users = int(E1.get())
    countA=0
    countB=0
    trainTimeUser=[]
    global trainsToA
    global trainsToB
   
    UsersList = []
    UserStartTime = []
    UserStartTimeString = []
    UsersStartStation = []
    # UsersStartStationLetter = []
    # UsersDestinationStationLetter = []
    UsersDestinationStation = []
    flat_list_A = []
    flat_list_D = []
    totalTime = []
    cabsTowardStation = []
    cabsTowardDestination = []
    # UsersTowardsB=[]
    # UsersTowardsA=[]
    trainTimeUserString=[]
    train_reach_time = []
    train_reach_time_string=[]

    UsersStationsFromA = []
    UsersStationsFromB = []

    numOfTrains = TrainTimetables(Users, TotalDuration, numOfStations, Iterations, TrainEvery_min, waitAtEndStop)

    print "\nnumber of trains required = "+str(numOfTrains)

    


    for i in xrange(numOfStations):
        UsersStationsFromA.append(0)
        UsersStationsFromB.append(0)

    for i in xrange(Users):
        cabsTowardStation.append(0)
        cabsTowardDestination.append(0)

    Atime, Btime, AtimeString, DtimeString = ([] for i in range(4)) 

    List_of_Lists = [UsersList,  UsersStartStation,  UsersDestinationStation, cabsTowardStation, AtimeString, trainTimeUserString, train_reach_time_string, cabsTowardDestination, DtimeString,  totalTime]

    for i in range(Users): #Users List
        UsersList.append("User "+str(i+1))

    
    

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
            train_reach_time.append(trainsToB[tempA][UsersDestinationStation[i]])
    
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
            train_reach_time.append(trainsToA[temp][(numOfStations) - UsersDestinationStation[i]-1])
    
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
        train_reach_time_string.append(dt.datetime.strftime(train_reach_time[i], frmt))
    
  
    ############################################# Assigning CABS TO USERS#######################
                    # -------cabs towards station-------
    sameTrainsFromA = dict((x, duplicates(trainTimeUserString, x)) for x in set(trainTimeUserString) if trainTimeUserString.count(x) > 1)
    trainCounterFromA = dict(Counter(trainTimeUserString))
    
    for keys in sameTrainsFromA.keys():
        
        c=trainCounterFromA[keys]
        # print c
        cabNo=random.randint(1,(c/3)+1)
        for i in sameTrainsFromA[keys]:
            cabsTowardStation[i] = "Cab No."+str(cabNo)+"|"+str(UsersStartStation[i])


    for i in xrange(Users):
        if cabsTowardStation[i]==0:
            cabsTowardStation[i] = "Cab No."+str(random.randint(1,(Users/3)+1))+"|"+str(UsersStartStation[i])

        # -------cabs towards Destination-------
    sameTrainsTowardsDestination = dict((x, duplicates(train_reach_time_string, x)) for x in set(train_reach_time_string) if train_reach_time_string.count(x) > 1)
    trainCounterTowardsDestination = dict(Counter(train_reach_time_string))

    for keys in sameTrainsTowardsDestination.keys():
        
        c=trainCounterTowardsDestination[keys]
        # print c
        cabNo=random.randint(1,(c/3)+1)
        for i in sameTrainsTowardsDestination[keys]:
            cabsTowardDestination[i] = "Cab No."+str(cabNo)+"||"+str(UsersDestinationStation[i])

    for i in xrange(Users):
        if cabsTowardDestination[i]==0:
            cabsTowardDestination[i] = "Cab No."+str(random.randint(1,(Users/3)+1))+"|"+str(UsersDestinationStation[i])

        
        
        
    



  


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

    print "\nNumber of people towards B = "+str(countA)
    print "\nNumber of people towards A = "+str(countB)
    print "-----Number of People at Every station going towards B----- "
    print UsersStationsFromA
    print "\n"
    print "-----Number of People at Every station going towards A----- "
    print UsersStationsFromB
  

if __name__ == '__main__':
    Users = input('Enter number of Users:  ')
    TotalDuration = input('Enter Duration of time to travel from one End to another(min):  ')
    numOfStations = input('Enter number of Stations:  ')
    Iterations = input('Enter number of Iterations:   ')
    TrainEvery_min = input('Enter Frequency of Train(min):  ')
    waitAtEndStop = input('Enter wait Time at each stop(min):  ')
    print "\n"
    # Users
#     TotalDuration = 60
# Iterations = 5
# waitAtEndStop = 15
# TrainEvery_min = 30

    main(Users, TotalDuration, numOfStations, Iterations, TrainEvery_min, waitAtEndStop)
    
 
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

