import datetime as dt
from random import sample
import random

frmt = '%d-%m-%Y %H:%M:%S'
# randomNumberPatition = random.randint(3,7)
# print str(randomNumberPatition) + "\n"
Users=30
UsersList=[]
UserStartTime=[]
UserStartTimeString=[]
UsersStartStation=[]
UsersStartStationLetter=[]
UsersDestinationStationLetter=[]
UsersDestinationStation=[]
flat_list_A=[]
flat_list_D=[]
totalTime=[]

Atime, Dtime, AtimeString, DtimeString= ([] for i in range(4)) 

List_of_Lists=[UsersList,  UsersStartStationLetter,  UsersDestinationStationLetter, AtimeString, DtimeString, totalTime]

for i in range(Users):
    UsersList.append("User "+str(i+1))

sample_date = dt.datetime(year=2018, month=10, day=6, hour=17, minute=00)

AtrainTime=sample_date
BtrainTime=AtrainTime + dt.timedelta(minutes=30)
CtrainTime=BtrainTime + dt.timedelta(minutes=30) 
DtrainTime=CtrainTime + dt.timedelta(minutes=30)
EtrainTime=DtrainTime + dt.timedelta(minutes=30)



# print UsersDestinationStation
# print UsersStartStation

for i in range(Users):
    UsersDestinationStation.append(random.randint(1,4))
    UsersStartStation.append(random.randint(0,UsersDestinationStation[i]-1))

    if UsersDestinationStation[i]==1:
        Atime.append(sample([sample_date - dt.timedelta(minutes=x, seconds=y) for x in range(3, 35) for y in range(0,60)],1))
        Dtime.append(sample([BtrainTime + dt.timedelta(minutes=x, seconds=y) for x in range(1, 28) for y in range(0,60)],1))
    
    elif UsersDestinationStation[i]==2:
        if UsersStartStation[i]==0:
            Atime.append(sample([sample_date - dt.timedelta(minutes=x, seconds=y) for x in range(3, 35) for y in range(0,60)],1))
            Dtime.append(sample([CtrainTime + dt.timedelta(minutes=x, seconds=y) for x in range(1, 28) for y in range(0,60)],1))
        else:
            Atime.append(sample([BtrainTime - dt.timedelta(minutes=x, seconds=y) for x in range(3, 28) for y in range(0,60)],1))
            Dtime.append(sample([CtrainTime + dt.timedelta(minutes=x, seconds=y) for x in range(1, 28) for y in range(0,60)],1))
   
    elif UsersDestinationStation[i]==3:
        if UsersStartStation[i]==0:
            Atime.append(sample([sample_date - dt.timedelta(minutes=x, seconds=y) for x in range(3, 35) for y in range(0,60)],1))
            Dtime.append(sample([DtrainTime + dt.timedelta(minutes=x, seconds=y) for x in range(1, 28) for y in range(0,60)],1))
        elif UsersStartStation[i]==1:
            Atime.append(sample([BtrainTime - dt.timedelta(minutes=x, seconds=y) for x in range(3, 28) for y in range(0,60)],1))
            Dtime.append(sample([DtrainTime + dt.timedelta(minutes=x, seconds=y) for x in range(1, 28) for y in range(0,60)],1))
        else:
            Atime.append(sample([CtrainTime - dt.timedelta(minutes=x, seconds=y) for x in range(3, 28) for y in range(0,60)],1))
            Dtime.append(sample([DtrainTime + dt.timedelta(minutes=x, seconds=y) for x in range(1, 28) for y in range(0,60)],1))
    
    else:
        if UsersStartStation[i]==0:
            Atime.append(sample([sample_date - dt.timedelta(minutes=x, seconds=y) for x in range(3, 35) for y in range(0,60)],1))
            Dtime.append(sample([EtrainTime + dt.timedelta(minutes=x, seconds=y) for x in range(1, 28) for y in range(0,60)],1))
        elif UsersStartStation[i]==1:
            Atime.append(sample([BtrainTime - dt.timedelta(minutes=x, seconds=y) for x in range(3, 28) for y in range(0,60)],1))
            Dtime.append(sample([EtrainTime + dt.timedelta(minutes=x, seconds=y) for x in range(1, 28) for y in range(0,60)],1))
        elif UsersStartStation[i]==2:
            Atime.append(sample([CtrainTime - dt.timedelta(minutes=x, seconds=y) for x in range(3, 28) for y in range(0,60)],1))
            Dtime.append(sample([EtrainTime + dt.timedelta(minutes=x, seconds=y) for x in range(1, 28) for y in range(0,60)],1))
        else:
            Atime.append(sample([DtrainTime - dt.timedelta(minutes=x, seconds=y) for x in range(3, 28) for y in range(0,60)],1))
            Dtime.append(sample([EtrainTime + dt.timedelta(minutes=x, seconds=y) for x in range(1, 28) for y in range(0,60)],1))




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
    td=(flat_list_D[i] - flat_list_A[i])
    hours, minutes = td.seconds // 3600, td.seconds // 60 % 60
    totalTime.append(str(hours)+" Hr "+str(minutes)+" min ")
    AtimeString.append(dt.datetime.strftime(flat_list_A[i], frmt))
    DtimeString.append(dt.datetime.strftime(flat_list_D[i], frmt))

for i in range(Users): #Users start stations
    if UsersStartStation[i]==0:
        UsersStartStationLetter.append("A")
    elif UsersStartStation[i]==1:
        UsersStartStationLetter.append("B")
    elif UsersStartStation[i]==2:
        UsersStartStationLetter.append("C")
    else:
        UsersStartStationLetter.append("D")

for i in range(Users): #Users end station
    if UsersDestinationStation[i]==1:
        UsersDestinationStationLetter.append("B")
    elif UsersDestinationStation[i]==2:
        UsersDestinationStationLetter.append("C")
    elif UsersDestinationStation[i]==3:
        UsersDestinationStationLetter.append("D")
    else:
        UsersDestinationStationLetter.append("E")



print "Train  from A ----" + str(AtrainTime)
print "Train  from B ----" + str(BtrainTime)
print "Train  from C ----" + str(CtrainTime)
print "Train  from D ----" + str(DtrainTime)
print "Train  from E ----" + str(EtrainTime)



print "\n\n" 
for a in zip(*List_of_Lists):
    print a










