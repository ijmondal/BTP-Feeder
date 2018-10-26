# from random import randrange
# import time
import random

print "Program running.."
Users=1000
Atime=[]
UsersList=[]
TrainTaken=[]
Btime=[]
finaltimetaken=[]
TrainJourneyTime=30
WaitTime=30
CabsToA=[]
CabsToB=[]

List_of_Lists=[UsersList,  Atime, Btime, CabsToA, TrainTaken, CabsToB, finaltimetaken]

for i in range(Users):
    UsersList.append("User "+str(i+1))

# print UsersList

for i in range(Users):
    Atime.append(random.randint(1,40))

# print Atime
# print "-------------------------------------------------------------------------------------------\n\n"

for i in range(Users):
    Btime.append(random.randint(1,40))

# print Btime
# print "-------------------------------------------------------------------------------------------\n\n"

for i in range(Users):
    if 20>=Atime[i]:
        finaltimetaken.append(Atime[i]+TrainJourneyTime+Btime[i])
        TrainTaken.append("5:30pm Train")
        CabsToA.append("Cab No."+str(random.randint(1,Users/3)) + " towards Station A")
        CabsToB.append("Cab No."+str(random.randint(1,Users/3))+"i towards station B")
    else:
        finaltimetaken.append((40-Atime[i])+Atime[i]+TrainJourneyTime+WaitTime+Btime[i])
        TrainTaken.append("6:00pm Train")
        CabsToA.append("Cab No."+str(random.randint(1,Users/3)) + "i towards Station A")
        CabsToB.append("Cab No."+str(random.randint(1,Users/3))+" towards station B")

# print finaltimetaken
# print "-------------------------------------------------------------------------------------------\n\n"


for a in zip(*List_of_Lists):
    print a

print "--Program terminated--"




