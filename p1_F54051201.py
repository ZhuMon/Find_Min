import sys
from functions import func
import threading

class MyRange():
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

        self.x_mid = (x_min+x_max)//2
        self.y_mid = (y_min+y_max)//2 

def fun_thread(t):
    global z_min
    for x in range(t.x_min, t.x_max):
        for y in range(t.y_min, t.y_max):
            z = func(x,y)
            if z < z_min:
                z_min = z

    


def brute(t):
    """
    input <MyRange> t
    """
    global z_min
    z_min = 9999

    t1 = MyRange(t.x_min, t.x_mid, t.y_min, t.y_mid)
    t2 = MyRange(t.x_mid, t.x_max, t.y_mid, t.y_max)
    a_th = threading.Thread(target=fun_thread, args=(t1,))
    b_th = threading.Thread(target=fun_thread, args=(t2,))
    a_th.start()
    b_th.start()
    a_th.join()
    b_th.join()

    return round(z_min,3)

def hill_climbing(point):
    for p in point:
        p[0]
        p[1]

def main():
    infile = open(sys.argv[1], "r")
    lines = infile.readlines()
    x_min = int(lines[0].split(',')[0])
    x_max = int(lines[0].split(',')[1])
    y_min = int(lines[1].split(',')[0])
    y_max = int(lines[1].split(',')[1])

    threshold = MyRange(x_min, x_max, y_min, y_max)

    init_num = int(lines[2])
    init_point = []
    for i in range(init_num):
        x = float(lines[3+i].split(',')[0])
        y = float(lines[3+i].split(',')[1])
        init_point.append([x,y])

    z_min = brute(threshold)
    z_min_climb = hill_climbing(init_point)
    # print(z_min)
    outfile = open(sys.argv[2], "w")
    outfile.write(str("{:.3f}".format(z_min)))
    

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Lose argument")
        sys.exit(1)
    main()
