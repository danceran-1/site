import math

def first_task(x,y,z):

    l_x = 4 ** (-0.25 * x) - (2 * math.sqrt(2)) ** (-4 / (3 * y)) * math.tan(4)
    l_y = math.cos(2 * math.atan(1 / (5 * z)) + math.atan(1 / 4))

    print(f'lx = {round((l_x),3)}')
    print(f'ly = {round((l_y),3)}\n')

    if abs(l_x) < 5 * abs(l_y):
    
        k_argument = abs(2 * l_x - 3 * math.e**(2 * l_y))
        k = math.log(k_argument)

    else:
        k_argument = abs(2 * l_x * (math.e**2) - 3 * l_y)
        k = math.log(k_argument)
       
    return k

if __name__=='__main__':

    x,y,z = 2.7, 1.83, -0.789
    out1 = first_task(x,y,z)
    print(f'k = {round((out1),4)}')