import sys
opr = sys.stdin.readline().strip().split(" ")
li = sys.stdin.readline().strip().split(" ")
li = [int(i) for i in li]
pan = []
bord_x = li[0]
bord_y = li[1]
f = -1
for i in range(bord_x):

    li1 = sys.stdin.readline().strip().split(" ")
    if "H" in li1:
        f = [i,li1.index("H")]
    pan.append(li1)

# print(f)
snacks = {}
direct = [0, -1]
y = f[0]
x = f[1]
len1 = 1
flag = True
# snacks[0] = "1"
for i in opr:
#     print(i == "U")
    if i == "U":
        direct[0] = -1
        direct[1] = 0
    elif i == "D":
        direct[0] = 1
        direct[1] = 0
    elif i == "L":
        direct[1] = -1
        direct[0] = 0
    elif i == "R":
        direct[1] = 1
        direct[0] = 0
    elif i == "G":
        snacks[0] = [y,x]
#         print("x1:" + str(x))
#         print("y1:" + str(y))
        x += direct[1]
        y += direct[0]
#         print("x2:" + str(x))
#         print("y2:" + str(y))
        if x >= bord_x or y >= bord_y or x < 0 or y < 0:
#             print("xx")
            break
#         print(pan[y][x])
#         print(direct)
        if pan[y][x] == "F":
#             print("F")
            for i in range(len(snacks)-1, 0, -1):
                snacks[i+1] = snacks[i]
            snacks[0] = [y,x]
#             print(len1)
            len1 += 1
            pan[y][x] == "E"

        else:
            for i in range(len(snacks)-1,0, -1):
                snacks[i] = snacks[i-1]
            snacks[0] = [y,x]

        for k,v in snacks.items():
            if k != 0:
                if v == snacks[0] :
                    flag = False
                    break
        if not flag:
            break


print(len1)
