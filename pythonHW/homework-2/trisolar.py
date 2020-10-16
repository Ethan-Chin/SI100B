from math import sqrt, pi, sin, cos

ERROR = 0.01


def AlmostEqual(first, second):
    delta = abs(ERROR * first)
    diff = abs(first - second)
    return diff <= delta



def task1(planets_num: int, check_time: int, bodys: list):

    location = []
    for i in bodys:
        location.append([i[1], i[2]]) # a result buffer
    for i in range(check_time):
        for ii in range(planets_num):
            for iii in range(planets_num): # update the velocity of this particle 
                deltaX = location[iii][0] - location[ii][0]
                deltaY = location[iii][1] - location[ii][1]
                if (not deltaX) and (not deltaY): # prevent it self to be caled in
                    continue
                scale = bodys[iii][0] / sqrt((deltaX**2 + deltaY**2)**3)
                bodys[ii][3] += scale*deltaX
                bodys[ii][4] += scale*deltaY # add each ponderance
            bodys[ii][1] += bodys[ii][3]
            bodys[ii][2] += bodys[ii][4] # update the location
        for i in range(planets_num):
            location[i][0] = bodys[i][1]
            location[i][1] = bodys[i][2]
    return location



def task2(check_time: int, bodys: list):

    sun = 0
    location = task1(4, check_time, bodys)
    for i in range(3):
        if sqrt((location[i][0] - location[3][0])**2 + (location[i][1] - location[3][1])**2) <= 200:
            sun += 1
    if sun == 0:
        return "Eternal Night"
    elif sun == 1:
        return "Stable Era"
    elif sun == 2:
        return "Double-Solar Day"
    elif sun == 3:
        return "Tri-Solar Day"



def task3(check_time: int, bodys: list):

    S = 0
    _bodys = []

    for i in range(check_time + 1):
        Era = task2(1, bodys)
        if Era == "Stable Era":
            S += 2
        else:
            S -= 1
        if S < 0:
            return "No civilization"

    if S < 400:
        return "level 1 civilization"
    elif S < 1200:
        return "level 2 civilization"
    else:
        return "level 3 civilization"


def task_bonus(check_time: int, bodys: list):

    day = 0
    theta = 0
    deltaTheta = pi / 180
    for i in range(1, check_time + 1):
        theta += deltaTheta
        normVec = [sin(theta), cos(theta)]
        if task2(1, bodys) == "Stable Era":
            sun0 = (bodys[0][1] - bodys[3][1])*normVec[0] + (bodys[0][2] - bodys[3][2])*normVec[1]
            sun1 = (bodys[1][1] - bodys[3][1])*normVec[0] + (bodys[1][2] - bodys[3][2])*normVec[1]
            sun2 = (bodys[2][1] - bodys[3][1])*normVec[0] + (bodys[2][2] - bodys[3][2])*normVec[1]
            if sun0 >= 0 and sun1 >= 0 and sun2 >= 0:
                day += 1
    return day


if __name__ == "__main__":
    '''
    Task 1 Example 1
    <planets-num> = 2, <check-time>  = 1986
    <planet1-mass> = 10000, <planet1-coordinate-x> = 0, <planet1-coordinate-y> = 0, <planet1-speed-x> = 0, <planet1-speed-y> = 0
    <planet2-mass> = 0.1, <planet2-coordinate-x> = 1000, <planet2-coordinate-y> = 0, <planet2-speed-x> = 0, <planet2-speed-y> = sqrt(10)
    '''
    output = task1(
        4,
        2,
        [
            [1, 0.01, 0, 0, 1000],
            [1, 0, 0, 1000, 0],
            [1, -0.01, 0, 0, 100],
            [0.1, 1, 0, 0, 0]
        ]
    )
    answer = [(-4.568800204932483e-09, 0.06283041322543657), (1000.0004568800274, -2.757889449272592)]
    print(output)
    for i in range(len(answer)):
        for j in (0, 1):
            ans = answer[i][j]
            out = output[i][j]
            AlmostEqual(ans, out)

    '''
    Task 2 Example 1
    <check-time>  = 1986
    <sun1-mass> = 1000, <sun1-coordinate-x> = 0, <sun1-coordinate-y> = 0, <sun1-speed-x> = 0, <sun1-speed-y> = 0
    <sun2-mass> = 1, <sun2-coordinate-x> = 1000000, <sun2-coordinate-y> = 0, <sun2-speed-x> = 0, <sun2-speed-y> = 0
    <sun3-mass> = 1, <sun3-coordinate-x> = -1000000, <sun3-coordinate-y> = 0, <sun3-speed-x> = 0, <sun3-speed-y> = 0
    <planet-mass> = 0.1, <planet-coordinate-x> = 100, <planet-coordinate-y> = 0, <planet-speed-x> = 0, <planet-speed-y> = sqrt(10)
    '''
    '''[1000, 0, 0, 0, 0],
            [1, 1000000, 0, 0, 0],
            [1, -1000000, 0, 0, 0],
            [0.1, 100, 0, 0, sqrt(10)]'''
            
    output = task2(
        2,
        [
            [1, 0, 0, 0, 1000],
            [1, 0, 0, 1000, 0],
            [1, 0, 0, 0, 100],
            [0.1, 1, 0, 0, 0]
        ]
    )
    print(output)

    '''
    Task 3 Example 1
    <check-time>  = 600
    <sun1-mass> = 1000, <sun1-coordinate-x> = 0, <sun1-coordinate-y> = 0, <sun1-speed-x> = 0, <sun1-speed-y> = 0
    <sun2-mass> = 0.001, <sun2-coordinate-x> = 148.6, <sun2-coordinate-y> = 0, <sun2-speed-x> = 0, <sun2-speed-y> = -2.59
    <sun3-mass> = 0.001, <sun3-coordinate-x> = 0, <sun3-coordinate-y> = 148.6, <sun3-speed-x> = 2.59, <sun3-speed-y> = 0
    <planet-mass> = 0.001, <planet-coordinate-x> = 0, <planet-coordinate-y> = -148.6, <planet-speed-x> = -2.59, <planet-speed-y> = sqrt(10)
    '''
    omega = 2*pi/360
    R = (1000/omega**2)**(1/3)
    output = task3(
        600,
        [
            [1000, 0, 0, 0, 0],
            [0.001, R, 0, 0, -omega*R],
            [0.001, 0, R, omega*R, 0],
            [0.001, 0, -R, -omega*R, 0]
        ]
    )
    print(output)
    # assert output == "level 3 civilization"

    '''
    Task BONUS Example 1
    <check-time>  = 6000
    <sun1-mass> = 1000, <sun1-coordinate-x> = 0, <sun1-coordinate-y> = 0, <sun1-speed-x> = 0, <sun1-speed-y> = 0
    <sun2-mass> = 0.001, <sun2-coordinate-x> = 148.6, <sun2-coordinate-y> = 0, <sun2-speed-x> = 0, <sun2-speed-y> = -2.59
    <sun3-mass> = 0.001, <sun3-coordinate-x> = 0, <sun3-coordinate-y> = 148.6, <sun3-speed-x> = 2.59, <sun3-speed-y> = 0
    <planet-mass> = 0.001, <planet-coordinate-x> = 0, <planet-coordinate-y> = -148.6, <planet-speed-x> = -2.59, <planet-speed-y> = sqrt(10)
    '''
    omega = 2*pi/360
    R = (1000/omega**2)**(1/3)
    output = task_bonus(
        6000,
        [
            [1000, 0, 0, 0, 0],
            [0.001, R, 0, 0, -omega*R],
            [0.001, 0, R, omega*R, 0],
            [0.001, 0, -R, -omega*R, 0]
        ]
    )
    print(output)
