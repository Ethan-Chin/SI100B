import re
temp = input().split()
flight_num = temp[0]
passenger_num = int(temp[1])
boarding_time = int(temp[2])
dptime = boarding_time
bus = []
Ctnr = []
bufr_cp = []
sizeBus = 0

input()
Olane_num = int(input())
Opsg = []

i = 0
while i < Olane_num:
    passenger = input().split()
    passenger[0] = int(passenger[0])
    if passenger[2] == flight_num:
        if re.search(r'CHD$', passenger[1]):
            bufr_cp.append(passenger)
            passenger = input().split()
            passenger[0] = int(passenger[0])
            bufr_cp.append(passenger)
            Opsg.append(bufr_cp)
            i = i + 1
            bufr_cp = []
        else:
            Opsg.append(passenger)
    i = i + 1


input()
Plane_num = int(input())
Ppsg = []
i = 0


while i < Plane_num:
    passenger = input().split()
    passenger[0] = int(passenger[0])
    if passenger[2] == flight_num:
        if re.search(r'CHD$', passenger[1]):
            passenger = tuple(passenger)
            bufr_cp.append(passenger)
            passenger = input().split()
            passenger[0] = int(passenger[0])
            passenger = tuple(passenger)
            bufr_cp.append(passenger)
            Ppsg.append(bufr_cp)
            i = i + 1
            bufr_cp = []
        else:
            passenger = tuple(passenger)
            Ppsg.append(passenger)
    i = i + 1



'''
Allp = Opsg + Ppsg



for i in range(len(Allp)):
    for j in range(len(Allp) - 1):
        if len(Allp[j]) == 2:
            arvt1 = Allp[j][1][0]
            tp1 = type(Allp[j][1])
        else:
            arvt1 = Allp[j][0]
            tp1 = type(Allp[j])
        if len(Allp[j + 1]) == 2:
            arvt2 = Allp[j][1][0]
            tp2 = type(Allp[j][1])
        else:
            arvt2 = Allp[j][0]
            tp2 = type(Allp[j])
        if (arvt1 > arvt2) or (arvt1 == arvt2 and (tp1 == list and tp2 == tuple)):
            t = Allp[j]
            Allp[j] = Allp[j + 1]
            Allp[j + 1] = t


for i in Allp:
    if len(i) == 2:
            time = i[1][0]
            sizeBus = sizeBus + 1
    else:
        time = i[0]
    if time <= dptime:
        bus.append(i)
        sizeBus = sizeBus + 1
    else:
        break
    if sizeBus == 20:
        break
    if sizeBus == 21:
        bus.pop()
        sizeBus = sizeBus - 2


for i in bus:
    if len(i) == 2:
        tp = type(i[0])
    else:
        tp = type(i)
    if tp == list:
        Opsg.remove(i)
    else:
        Ppsg.remove(i)

'''
while Opsg or Ppsg:

    while Ppsg and sizeBus != 20:
        if sizeBus == 21:
            Ctnr.append(bus.pop())
            sizeBus = sizeBus - 2
        if len(Ppsg[0]) == 2:
            if Ppsg[0][1][0] <= dptime:
                bus.append(Ppsg[0])
                Ppsg.remove(Ppsg[0])
                sizeBus = sizeBus + 2
            else:
                break
        else:
            if Ppsg[0][0] <= dptime:
                bus.append(Ppsg[0])
                Ppsg.remove(Ppsg[0])
                sizeBus = sizeBus + 1
            else:
                break


    while Opsg and sizeBus != 20:
        if sizeBus == 21:
            Ctnr.append(bus.pop())
            sizeBus = sizeBus - 2
        if len(Opsg[0]) == 2:
            if Opsg[0][1][0] <= dptime:
                bus.append(Opsg[0])
                Opsg.remove(Opsg[0])
                sizeBus = sizeBus + 2
            else:
                break
        else:
            if Opsg[0][0] <= dptime:
                bus.append(Opsg[0])
                Opsg.remove(Opsg[0])
                sizeBus = sizeBus + 1
            else:
                break

    if bus:
        earlest = dptime
    while (Opsg or Ppsg) and sizeBus != 20:
        #if bus:
            #if len(bus[0]) == 2:
            #    earlest = bus[0][0][0]
            #else:
            #    earlest = bus[0][0]
            #for i in bus:
            #    if len(i) == 2:
            #        time = i[0][0]
            #    else:
            #        time = i[0]
            #    if time < earlest:
            #        earlest = time
            #earlest = dptime
        if not bus:
            if not Ppsg and Opsg:
                if len(Opsg[0]) == 2:
                    #earlest = Opsg[0][0][0]
                    earlest = Opsg[0][1][0]
                else:
                    earlest = Opsg[0][0]
            elif not Opsg and Ppsg:
                if len(Ppsg[0]) == 2:
                    #earlest = Ppsg[0][0][0]
                    earlest = Ppsg[0][1][0]
                else:
                    earlest = Ppsg[0][0]
            else:
                if len(Opsg[0]) == 2:
                    #earlest1 = Opsg[0][0][0]
                    earlest1 = Opsg[0][1][0]
                else:
                    earlest1 = Opsg[0][0]
                if len(Ppsg[0]) == 2:
                    #earlest2 = Ppsg[0][0][0]
                    earlest2 = Ppsg[0][1][0]
                else:
                    earlest2 = Ppsg[0][0]
                earlest = min(earlest1, earlest2)
        if not Ppsg and Opsg:
            if len(Opsg[0]) == 2 and Opsg[0][1][0] - earlest <= 600:
                bus.append(Opsg[0])
                sizeBus = sizeBus + 2
                dptime = Opsg[0][1][0]
                Opsg.remove(Opsg[0])
            elif len(Opsg[0]) == 3 and Opsg[0][0] - earlest <= 600:
                bus.append(Opsg[0])
                sizeBus = sizeBus + 1
                dptime = Opsg[0][0]
                Opsg.remove(Opsg[0])
            else:
                dptime = earlest + 600
                break
        elif not Opsg and Ppsg:
            if len(Ppsg[0]) == 2 and Ppsg[0][1][0] - earlest <= 600:
                bus.append(Ppsg[0])
                sizeBus = sizeBus + 2
                dptime = Ppsg[0][1][0]
                Ppsg.remove(Ppsg[0])
            elif len(Ppsg[0]) == 3 and Ppsg[0][0] - earlest <= 600:
                bus.append(Ppsg[0])
                sizeBus = sizeBus + 1
                dptime = Ppsg[0][0]
                Ppsg.remove(Ppsg[0])
            else:
                earlest = earlest + 600
                break
        elif Opsg and Ppsg:
            if len(Opsg[0]) == 2:
                dtime1 = Opsg[0][1][0]
            else:
                dtime1 = Opsg[0][0]
            if len(Ppsg[0]) == 2:
                dtime2 = Ppsg[0][1][0]
            else:
                dtime2 = Ppsg[0][0]
            if dtime2 <= dtime1 and (dtime2 - earlest <= 600):
                bus.append(Ppsg[0])
                dptime = dtime2
                if len(Ppsg[0]) == 2:
                    sizeBus = sizeBus + 2
                else:
                    sizeBus = sizeBus + 1
                Ppsg.remove(Ppsg[0])
            elif dtime2 > dtime1 and (dtime1 - earlest <= 600):
                bus.append(Opsg[0])
                dptime = dtime1
                if len(Opsg[0]) == 2:
                    sizeBus = sizeBus + 2
                else:
                    sizeBus = sizeBus + 1
                Opsg.remove(Opsg[0])
            else:
                dptime = earlest + 600
                break
        if sizeBus == 21:
            Ctnr.append(bus.pop())
            sizeBus = sizeBus - 2
    if Ctnr:
        Ctnr.reverse()
        for i in Ctnr:
            if type(i[0]) == tuple:
                Ppsg.insert(0, i)
            else:
                Opsg.insert(0, i)
        Ctnr = []

    
    print('%d%s' % (dptime, ':'), end = '')
    for i in bus:
        if len(i) == 2:
            print(' ' + i[0][1], end = '')
            print(' ' + i[1][1], end = '')
        else:
            print(' ' + i[1], end = '')
    print()
    bus = []
    sizeBus = 0
    dptime = dptime + 600




