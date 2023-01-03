#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
#import cvxpy  as cp

import sys, os                                          #for path to external scripts
script_dir = os.path.dirname(__file__)
lib_relative = '../../../CoordGeo'
fig_relative = '../figs/fig1.pdf'
sys.path.insert(0,'/sdcard/Download/CoordGeo/CoordGeo')

#if using termux
import subprocess
import shlex
#end if
#Defining f(x)
def f(x,a):
	return (x+a *np.sin(2*x))
a = 1
label_str = "$x+sin2*x$"

#For maxima using gradient ascent
cur_x = 3.5
cur_y=0.5
alpha = 0.001 
precision = 0.00000001 
previous_step_size = 1
max_iters = 100000000 
iters = 0

#Defining derivative of f(x)
df = lambda x: 1+2*a*np.cos(2*x)

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
    prev_x = cur_x             
    cur_x += alpha * df(prev_x)   
    previous_step_size = abs(cur_x - prev_x)   
    iters+=1  

max_val = f(cur_x,a)
print("Maximum value of f(x) is ", max_val, "at","x =",cur_x)

#Gradient ascent calculation
while (previous_step_size > precision) & (iters < max_iters) :
      prev_y = cur_y
      cur_y -= alpha * df(prev_y)
      previous_step_size = abs(cur_y - prev_y)
      iters+=1
 
min_val = f(cur_y,a)
print("Minimum value of f(x) is ", min_val, "at","x =",cur_y)

#Plotting f(x)
x=np.linspace(0,7,100)
y=f(x,a)
plt.plot(x,y,label=label_str)
#Labelling points
plt.plot(cur_x,max_val,'o')
plt.text(cur_x, max_val,f'P({cur_x:.4f},{max_val:.4f})')
plt.plot(cur_y,min_val,'o')
plt.text(cur_y, min_val,f'Q({cur_y:.4f},{min_val:.4f})')

plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.grid()
plt.legend()

#if using termux
plt.savefig('/sdcard/Download/fwc/optimization/opt.pdf')
subprocess.run(shlex.split("termux-open /sdcard/Download/fwc/optimization/opt.pdf"))
#else
plt.show()


