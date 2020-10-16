temp = input().split()
flight_num = temp[0]
passenger_num = int(temp[1])
boarding_time = int(temp[2])
input()
Olane_num = int(input())
Opsg = []
for i in range(Olane_num):
    passenger = input().split()
    passenger[0] = int(passenger[0])
    if passenger[2] == flight_num:
        Opsg.append(passenger)
backtime = boarding_time
while len(Opsg) >= 20:
    if Opsg[19][0] > backtime:
        aptime = Opsg[19][0]
    else:
        aptime = backtime
    print('%d%s' % (aptime, ':'), end = '')
    for i in range(20):
        print(' ' + Opsg[0][1], end = '')
        Opsg.remove(Opsg[0])
    print()
    backtime = aptime + 600
if Opsg:
    if Opsg[len(Opsg) - 1][0] > backtime:
        aptime = Opsg[len(Opsg) - 1][0]
    else:
        aptime = backtime
    print('%d%s' % (aptime, ':'), end = '')
    for i in range(len(Opsg)):
        print(' ' + Opsg[i][1], end='')
    print()
