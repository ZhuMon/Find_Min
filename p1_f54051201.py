import sys
from functions import func

class MyRange():
    def __init__(self, x_min, x_max, y_min, y_max):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max

def brute(t):
    """
    input <MyRange> t
    output <Float> z_min
    """
    z_min = 9999
    
    # count execution of func() 
    count_func = 0

    for x in range(t.x_min, t.x_max):
        for y in range(t.y_min, t.y_max):
            z = func(x,y)
            count_func += 1
            if z < z_min:
                z_min = z
    print("Brute: {0}".format(count_func))

    return round(z_min,3)

def hill_climbing(x, y, t, step):
    # count execution of func() 
    count_func = 0

    z_min = func(x, y)
    count_func += 1

    while True:
        now_z_min = z_min # for check whether break the loop

        # climb left
        if x-step >= t.x_min:
            z = func(x-step, y)
            count_func += 1
            if z < z_min:
                x = x-step
                z_min = z

        # climb right
        if x+step <= t.x_max:
            z = func(x+step, y)
            count_func += 1
            if z < z_min:
                x = x+step
                z_min = z

        # climb up
        if y+step <= t.y_max:
            z = func(x, y+step)
            count_func += 1
            if z < z_min:
                y = y+step
                z_min = z

        # climb down
        if y-step >= t.y_min:
            z = func(x, y-step)
            count_func += 1
            if z < z_min:
                y = y-step
                z_min = z

        if now_z_min == z_min:
            break
    return z_min, count_func
    

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
    aver_fun_count = 0
    for i in range(init_num):
        x = int(lines[3+i].split(',')[0])
        y = int(lines[3+i].split(',')[1])
        z_min, func_count = hill_climbing(x, y, threshold, 1)
        print("({0:-3d},{1:-3d})\t{2}\t{3:.3f}".format(x,y,func_count, z_min))
        outfile.write("{:.3f}\n".format(z_min))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: \n\tpython3 {0} <input file> <output file>".format(sys.argv[0]))
        sys.exit(1)
    main()
