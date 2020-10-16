temp = input().split()
flight_num = temp[0]
passenger_num = int(temp[1])
boarding_time = int(temp[2])
dptime = boarding_time
input()
Olane_num = int(input())
bus = []
Opsg = []
for i in range(Olane_num):
    passenger = input().split()
    passenger[0] = int(passenger[0])
    if passenger[2] == flight_num:
    #if passenger[0] <= dptime:
            #bus.append(passenger)
        #else:
        Opsg.append(passenger)
input()
Plane_num = int(input())
Ppsg = []
for i in range(Plane_num):
    passenger = input().split()
    passenger.append(' ')
    passenger[0] = int(passenger[0])
    if passenger[2] == flight_num:
    #if passenger[0] <= dptime:
            #bus.append(passenger)
        #else:
        Ppsg.append(passenger)
'''for i in range(len(bus)):
    for j in range(len(bus) - 1):
        if (bus[j][0] > bus[j + 1][0]) or (bus[j][0] == bus[j + 1][0] and (len(bus[j]) < len(bus[j + 1]))):
            t = bus[j]
            bus[j] = bus[j + 1]
            bus[j + 1] = t
if len(bus) > 20:
    back = bus[20:].reverse()
    for i in back:
        if len(i) == 3:
            Opsg.insert(0, i)
        else:
            Ppsg.insert(0, i)'''
while Opsg or Ppsg:
    if Ppsg:
        while Ppsg[0][0] <= dptime and len(bus) < 20:
            bus.append(Ppsg[0])
            Ppsg.remove(Ppsg[0])
            if not Ppsg:
                break
    if Opsg:
        while Opsg[0][0] <= dptime and len(bus) < 20:
            bus.append(Opsg[0])
            Opsg.remove(Opsg[0])
            if not Opsg:
                break
    if bus:
        earlest = dptime
    while len(bus) < 20 and (Opsg or Ppsg):
        #if bus:
            #earlest = bus[0][0]
            #for i in bus:
            #    if i[0] < earlest:
            #        earlest = i[0]
            #print(dptime)
            #earlest = dptime
        if not bus:
            if not Ppsg and Opsg:
                earlest = Opsg[0][0]
            elif not Opsg and Ppsg:
                earlest = Ppsg[0][0]
            else:
                earlest = min(Opsg[0][0], Ppsg[0][0])
        if not Ppsg and Opsg:
            if Opsg[0][0] - earlest <= 600:
                bus.append(Opsg[0])
                dptime = Opsg[0][0]
                Opsg.remove(Opsg[0])
            else:
                dptime = earlest + 600
                break
        elif not Opsg and Ppsg:
            if Ppsg[0][0] - earlest <= 600:
                bus.append(Ppsg[0])
                dptime = Ppsg[0][0]
                Ppsg.remove(Ppsg[0])
            else:
                dptime = earlest + 600
                break
        elif Opsg and Ppsg:
            if Ppsg[0][0] <= Opsg[0][0] and (Ppsg[0][0] - earlest <= 600):
                bus.append(Ppsg[0])
                dptime = Ppsg[0][0]
                Ppsg.remove(Ppsg[0])
            elif Ppsg[0][0] > Opsg[0][0] and (Opsg[0][0] - earlest <= 600):
                bus.append(Opsg[0])
                dptime = Opsg[0][0]
                Opsg.remove(Opsg[0])
            else:
                dptime = earlest + 600
                break
    print('%d%s' % (dptime, ':'), end = '')
    for i in bus:
        print(' ' + i[1], end = '')
    print()
    bus = []
    dptime = dptime + 600