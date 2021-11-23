import copy

import get_coordinates2


def FindCenter(input):
    loc = copy.deepcopy(input)
    for x in loc:
        center_x = (x[1][0]+x[0][0])/2
        center_y = (x[3][1]+x[0][1])/2
        center = [center_x, center_y]
        x.append(center)
    # print("location:",loc)
    return(loc)


def DecideRange(input):
    return(abs(input[0][1][0]-input[0][0][0]))


def DetectNeighbour(ids, input):
    location = FindCenter(input)
    range = DecideRange(input)
    elem = []
    # print(range)
    for i, id in enumerate(ids):
        lists = [i, id, -1, -1, -1, -1]
        for j, destid in enumerate(ids):
            if j == i:
                continue
            if (location[i][0][0] <= location[j][4][0] <= (location[i][0][0]+range)) and ((location[i][0][1]-range) <= location[j][4][1] <= location[i][0][1]):
                lists[2] = j
            elif (location[i][1][0] <= location[j][4][0] <= (location[i][1][0]+range)) and ((location[i][0][1]+range) >= location[j][4][1] >= location[i][0][1]):
                lists[3] = j
            elif (location[i][2][0] >= location[j][4][0] >= (location[i][2][0]-range)) and ((location[i][2][1]+range) >= location[j][4][1] >= location[i][2][1]):
                lists[4] = j
            elif (location[i][3][0] >= location[j][4][0] >= (location[i][3][0]-range)) and ((location[i][3][1]-range) <= location[j][4][1] <= location[i][3][1]):
                lists[5] = j
        elem.append(lists)
    return(elem)


def GetDestination(elem):
    destination = []
    for i in range(len(elem)):
        if elem[i][1] == 0:  # 角のidを0としてスキップ
            continue

        if elem[i][1] == 1:
            elem_name = "Source"
        elif elem[i][1] == 2:
            elem_name = "Resistor"
        elif elem[i][1] == 3:
            elem_name = "Capacitor"

        if elem[i][3] >= 0 or elem[i][5] >= 0:
            destination.append([elem[i][0], elem_name, "Right"])
        elif elem[i][2] >= 0:
            destination.append([elem[i][0], elem_name, "Up"])
        elif elem[i][4] >= 0:
            destination.append([elem[i][0], elem_name, "Down"])
    return(destination)


def GetConnection(elem):
    connected = []
    for i in range(len(elem)):
        for j in range(2, 6):
            if elem[i][0] >= elem[i][j]:
                continue
            if elem[elem[i][j]][1] == 0:  # 角のidを0とする
                for k in range(2, 6):
                    if elem[elem[i][j]][k] >= 0 and elem[elem[i][j]][k] != elem[i][0]:
                        connected.append(elem[i][0], elem[elem[i][j]][k])
            else:
                connected.append([elem[i][0], elem[i][j]])
    return(connected)


def WriteText(ids, input) -> str:
    elem = DetectNeighbour(ids, input)
    destination = GetDestination(elem)
    connection = GetConnection(elem)
    # print(elem)
    result = f"{len(destination)} {len(connection)}"
    for i in destination:
        result += f"\n{i[0]} {i[1]} {i[2]}"
    for i in connection:
        result += f"\n{i[0]} {i[1]}"
    return result


if __name__ == "__main__":
    # テスト用↓
    #ids = [1,2]
    #input = [[[114,114],[263,114],[263,263],[114,263]],[[300,114],[449,114],[449,263],[300,263]]]
    #input = [[[114,114],[263,114],[263,263],[114,263]],[[114,300],[263,300],[263,449],[114,449]]]

    ids, input = get_coordinates2.main()
    WriteText(ids, input)
