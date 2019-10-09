import sys
from functions import func

def myRound(x, n):
    a = x * (10 ** n)
    if a - int(a) >= 0.5:
        b = int(a) + 1
        return b * (10 ** (0-n))
    else:
        b = int(a)
        return b * (10 ** (0-n))

def brute(x_min, x_max, y_min, y_max):
    z_min = 9999
    for x in range(x_min, x_max):
        for y in range(y_min, y_max):
            z = func(x,y)
            if z < z_min:
                z_min = z

    return z_min

def main():
    infile = open(sys.argv[1], "r")
    lines = infile.readlines()
    x_min = int(lines[0].split(',')[0])
    x_max = int(lines[0].split(',')[1])
    y_min = int(lines[1].split(',')[0])
    y_max = int(lines[1].split(',')[1])
    init_num = int(lines[2])
    init_point = []
    for i in range(init_num):
        x = float(lines[3+i].split(',')[0])
        y = float(lines[3+i].split(',')[1])
        init_point.append([x,y])

    z_min = brute(x_min, x_max, y_min, y_max)
    print(z_min)
    outfile = open(sys.argv[2], "w")
    outfile.write(str("{:.3f}".format(z_min)))
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Lose argument")
        sys.exit(1)
    main()
