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
    output <Float> z_min
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

def hill_climbing(x, y, t, step):
    
    z_min = func(x, y)

    while True:
        now_z_min = z_min

        # climb left
        if x-step >= t.x_min:
            z = func(x-step, y)
            if z < z_min:
                x = x-step
                z_min = z

        # climb right
        if x+step <= t.x_max:
            z = func(x+step, y)
            if z < z_min:
                x = x+step
                z_min = z

        # climb up
        if y+step <= t.y_max:
            z = func(x, y+step)
            if z < z_min:
                y = y+step
                z_min = z

        # climb down
        if y-step >= t.y_min:
            z = func(x, y-step)
            if z < z_min:
                y = y-step
                z_min = z

        if now_z_min == z_min:
            break

    return z_min
    

def main():
    infile = open(sys.argv[1], "r")
    outfile = open(sys.argv[2], "w")

    lines = infile.readlines()
    x_min = int(lines[0].split(',')[0])
    x_max = int(lines[0].split(',')[1])
    y_min = int(lines[1].split(',')[0])
    y_max = int(lines[1].split(',')[1])

    # put range into my class: MyRange
    threshold = MyRange(x_min, x_max, y_min, y_max)
    
    # do brutal formula
    z_min = brute(threshold)
    outfile.write("{:.3f}\n".format(z_min))

    # read init point and do hill_climbing
    init_num = int(lines[2])
    init_point = []
    for i in range(init_num):
        x = int(lines[3+i].split(',')[0])
        y = int(lines[3+i].split(',')[1])
        z_min = hill_climbing(x, y, threshold, 1)
        outfile.write("{:.3f}\n".format(z_min))
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: \n\tpython3 {0} <input file> <output file>".format(sys.argv[0]))
        sys.exit(1)
    main()
