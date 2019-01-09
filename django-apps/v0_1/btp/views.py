# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

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


# startTimefromA = dt.datetime(2019,1,10,5,00,00,00)


def index(request):
    if request.method == "POST" :
        trainsToB=[]
        trainsToA=[]
        trainsToBstring=[]
        trainsToAstring=[]

        
        data = request.POST

            
        Users = int(data.get('Users'))
        TotalDuration = int(data.get('TotalDuration'))
        numOfStations = int(data.get('numOfStations'))
        Iterations = int(data.get('Iterations'))
        TrainEvery_min = int(data.get('TrainEvery_min'))
        waitAtEndStop = int(data.get('waitAtEndStop'))


        # ----------------- All the main variables are declared here----------------------------
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
        CabsSpeedDestList = []
        CabsSpeedStationList = []
        AtimeGap=[]
        AusersDist=[]
        BtimeGap=[]
        BusersDist=[]
        
            
    # --------------------------------------------------------end of declaring variables---------------------------
        numOfTrains = TrainTimetables(Users, TotalDuration, numOfStations, Iterations, TrainEvery_min, waitAtEndStop, trainsToAstring, trainsToBstring, trainsToA, trainsToB)
    

        print "\nnumber of trains required = "+str(numOfTrains)

        

    #array initiation to find number of people going to and from every station
        for i in xrange(numOfStations):
            UsersStationsFromA.append(0)
            UsersStationsFromB.append(0)

    # array initiation for Cab lists
        for i in xrange(Users):
            cabsTowardStation.append(0)
            cabsTowardDestination.append(0)
            CabsSpeedDestList.append(0)
            CabsSpeedStationList.append(0)
            AusersDist.append(0)

        Atime, Btime, AtimeString, DtimeString = ([] for i in range(4)) 

        

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
                cabsTowardStation[i] = "Cab No."+str(cabNo)+"||"+str(UsersStartStation[i])


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

        # -----------Assigning speed of Cabs in km/h-------------

        # Assigning speed for cabs towards destination

        myset = list(sorted(set(cabsTowardDestination)))        
        CabsSpeedDestDict = {}
        for i in range(len(myset)):
            CabsSpeedDestDict[myset[i]]= random.randint(10,40)

        for i in xrange(Users):
            if cabsTowardDestination[i] in CabsSpeedDestDict:
                CabsSpeedDestList[i]=CabsSpeedDestDict[cabsTowardDestination[i]]

    # Assigning speed for cabs towards station

        myset2 = list(sorted(set(cabsTowardStation)))
        CabsSpeedStationDict = {}
        for i in range(len(myset2)):
            CabsSpeedStationDict[myset2[i]]= random.randint(10,40)

        for i in xrange(Users):
            if cabsTowardStation[i] in CabsSpeedStationDict:
                CabsSpeedStationList[i]=CabsSpeedStationDict[cabsTowardStation[i]]

        
        # -----------Calculating Distances of Users from the Stations in meters-------------

        for i in xrange(Users):
            AtimeGap.append(trainTimeUser[i]-flat_list_A[i])
        for i in xrange(Users):
            AusersDist[i]=(AtimeGap[i].total_seconds()/3600) * CabsSpeedStationList[i]

        # for i in xrange(Users):
        #     BtimeGap.append(train_reach_time[i]-flat_list_D[i])
        # for i in xrange(Users):
        #     BusersDist[i]=(BtimeGap[i].total_seconds()/3600) * CabsSpeedDestList[i]

        
        # print "\n\n" 
# List_of_Lists = [UsersList,  UsersStartStation,  UsersDestinationStation, cabsTowardStation, CabsSpeedStationList, AusersDist, AtimeString, trainTimeUserString, train_reach_time_string, cabsTowardDestination, CabsSpeedStationList, DtimeString,  totalTime]

        UsersStartStationString = [str(i) for i in UsersStartStation]
        
        List_of_Lists = [UsersList,  UsersStartStationString,  UsersDestinationStation, cabsTowardStation, CabsSpeedStationList, AusersDist, AtimeString, trainTimeUserString, train_reach_time_string, cabsTowardDestination, CabsSpeedDestList, DtimeString, totalTime]
        main_list = zip(*List_of_Lists)

        print main_list
        print "\n"
        for a in zip(*List_of_Lists):
            print a

        print "\nNumber of people towards B = "+str(countA)
        print "\nNumber of people towards A = "+str(countB)
        print "-----Number of People at Every station going towards B----- "
        print UsersStationsFromA
        print "\n"
        print "-----Number of People at Every station going towards A----- "
        print UsersStationsFromB
        
        # for i in xrange(nu)
        data1={
            'countA':countA,
            'countB':countB,
            'UsersStationsFromA':UsersStationsFromA,
            'UsersStationsFromB':UsersStationsFromB,
            'Users':Users,
            'TotalDuration':TotalDuration,
            'numOfStations':numOfStations,
            'Iterations':range(Iterations),
            'TrainEvery_min':TrainEvery_min,
            'waitAtEndStop':waitAtEndStop,
            'UsersList':UsersList,
            'UsersStartStation':UsersStartStation,
            'UsersDestinationStation':UsersDestinationStation,
            'cabsTowardStation':cabsTowardStation,
            'CabsSpeedStationList':CabsSpeedStationList,
            'AusersDist':AusersDist,
            'AtimeString':AtimeString,
            'trainTimeUserString':trainTimeUserString,
            'train_reach_time_string':train_reach_time_string,
            'cabsTowardDestination':cabsTowardDestination,
            'CabsSpeedDestList':CabsSpeedDestList,
            # 'BusersDist':BusersDist,
            'DtimeString':DtimeString,
            'totalTime':totalTime,
            'trainsToAstring':trainsToAstring,
            'trainsToBstring':trainsToBstring,
            'numOfTrains':numOfTrains,
            'List_of_Lists':List_of_Lists,
            'main_list':main_list,
        }
        print len(data1['Iterations'])
        return render(request, 'timetable.html',context={'data':data1,'n':["Station "+str(i+1) for i in range(numOfStations)]
        })
#  Users = int(data.get('Users'))
#         TotalDuration = int(data.get('TotalDuration'))
#         numOfStations = int(data.get('numOfStations'))
#         Iterations = int(data.get('Iterations'))
#         TrainEvery_min = int(data.get('TrainEvery_min'))
#         waitAtEndStop = int(data.get('waitAtEndStop'))

        
    
    
    return render(request, 'index.html')

def TrainTimetables(Users, TotalDuration, numOfStations, Iterations, TrainEvery_min, waitAtEndStop, trainsToAstring, trainsToBstring, trainsToA, trainsToB):
    #Calculating optimal number of trains required
    # trainsToAstring
    # trainsToBstring
    startTimefromA = dt.datetime(2018,10,27,10,00,00,00)
    startTime = startTimefromA
    endTime = startTime + dt.timedelta(minutes=TotalDuration)
    nextTrain = endTime + dt.timedelta(minutes=waitAtEndStop)

    beforeTrain = startTime - dt.timedelta(minutes=TotalDuration - waitAtEndStop)
    time_elapsed=nextTrain - beforeTrain
    numOfTrains = int(time_elapsed.total_seconds()/(TrainEvery_min*60))

    startTimefromB = beforeTrain
    
    # Creating timetables for both upward and downward journey
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

# printing TrainTimetables --- printed while calling the function
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


# def main(request):







