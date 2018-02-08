import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def stepGradient(b_current, m_current, points, learningRate):
    b_gradient = 0
    m_gradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        b_gradient += -(2/N) * (points[i][1] - ((m_current*points[i][0]) + b_current))
        m_gradient += -(2/N) * points[i][0] * (points[i][1] - ((m_current * points[i][0]) + b_current))
    new_b = b_current - (learningRate * 100 * b_gradient)
    new_m = m_current - (learningRate * m_gradient)
    return [new_b, new_m]

def get_primes(number, offset, randomness):
    i=0
    rand=list(np.random.randint(-20,20,number))
    while i<number:
        yield offset+rand[i]*randomness+i*0.3
        i += 1

rand_y=list(get_primes(30,7,0.15))
rand_x=list(get_primes(30,7,0.15))
points=list(zip(rand_x, rand_y))
points_list=stepGradient(0.0, 0.0, points, 0.0005)

def update_line(num,points_list,  line):
    points_list1=stepGradient(points_list[0], points_list[1], points, 0.0002)
    points_list[1]=points_list1[1]
    points_list[0]=points_list1[0]
    line.set_data(list(range(22)),[points_list[1]*i+points_list[0] for i in range(22)]),
    return line,

fig1 = plt.figure()

# Fixing random state for reproducibility

l, = plt.plot([], [], 'r-')
plt.plot(rand_x, rand_y, 'ro')
plt.xlim(0, 20)
plt.ylim(0, 20)
plt.ylabel('y')
plt.xlabel('x')
plt.title('Gradient Descent example')
line_ani = animation.FuncAnimation(fig1, update_line, 100, fargs=(points_list, l),
                                   interval=50, blit=True)

# To save this second animation with some metadata, use the following command:
# im_ani.save('im.mp4', metadata={'artist':'Guido'})

plt.show()