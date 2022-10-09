from turtle import width
import numpy as np
import matplotlib.pyplot as plt
import sys
import math

# traj1 = np.loadtxt('controller_output/trajectory_run1.txt',delimiter=',')
# traj2 = np.loadtxt('controller_output/trajectory_run2.txt',delimiter=',')
# traj3 = np.loadtxt('controller_output/trajectory_run3.txt',delimiter=',')
# traj4 = np.loadtxt('controller_output/trajectory_run4.txt',delimiter=',')
traj5 = np.loadtxt('controller_output/trajectory_run5.txt',delimiter=',')
traj6 = np.loadtxt('controller_output/trajectory_run6.txt',delimiter=',')
# traj7 = np.loadtxt('controller_output/trajectory_run7.txt',delimiter=',')

# opt_racing_line = np.loadtxt('../waypoints_new.csv',delimiter=',')

file_centre_line='racetrack_waypoints.txt'
if file_centre_line != None:
    centre_line = np.loadtxt(file_centre_line,delimiter = ",")
else :
    centre_line=None
# centre_line[:,1] = -centre_line[:,1]
tx_center, ty_center, tyaw_center = centre_line[:-1,0], centre_line[:-1,1], np.arctan2(centre_line[1:,1]-centre_line[:-1,1],centre_line[1:,0]-centre_line[:-1,0])

# Start line
plt.plot([tx_center[0]+np.cos(tyaw_center[0]+math.pi/2),tx_center[0]-np.cos(tyaw_center[0]+math.pi/2)],[ty_center[0]+np.sin(tyaw_center[0]+math.pi/2),ty_center[0]-np.sin(tyaw_center[0]+math.pi/2)],linewidth=5.0,color='green')#,marker='o')
plt.text(tx_center[0],ty_center[0],'Start line')

# Finish line
plt.plot([tx_center[-1]+np.cos(tyaw_center[-1]+math.pi/2),tx_center[-1]-np.cos(tyaw_center[-1]+math.pi/2)],[ty_center[-1]+np.sin(tyaw_center[-1]+math.pi/2),ty_center[-1]-np.sin(tyaw_center[-1]+math.pi/2)],linewidth=5.0,color='red')#,marker='o')
plt.text(tx_center[-1],ty_center[-1],'End line')

# plt.plot(-372,65,-358,65,marker='o',size=5)

left_boundary = np.array([tx_center-7*np.sin(tyaw_center),ty_center+7*np.cos(tyaw_center)]).T
right_boundary = np.array([tx_center+7*np.sin(tyaw_center),ty_center-7*np.cos(tyaw_center)]).T
# plt.plot(opt_racing_line[:,0],-opt_racing_line[:,1],'--',label="Optimal racing line")
plt.plot(left_boundary[:,0],left_boundary[:,1],'--',label="Track left boundary")
plt.plot(right_boundary[:,0],right_boundary[:,1],'--',label="Track right boundary")
# plt.plot(traj1[:,0],traj1[:,1],'-',label="Followed trajectory (iter 1)")
# plt.plot(traj2[:,0],traj2[:,1],'-',label="Followed trajectory (iter 2)")
# plt.plot(traj3[:,0],traj3[:,1],'-',label="Followed trajectory (iter 3)")
# plt.plot(traj4[:,0],traj4[:,1],'-',label="Followed trajectory (iter 4)")
plt.plot(traj5[:,0],traj5[:,1],'-',label="Followed trajectory (iter 5)")
plt.plot(traj6[:,0],traj6[:,1],'-',label="Followed trajectory (iter 6)")
# plt.plot(traj7[:,0],traj7[:,1],'-',label="Followed trajectory (iter 7)")
plt.plot(tx_center,ty_center,'-',label="Center line (ref)")
# plt.plot(traj_with_comp[:,0],traj_with_comp[:,1],'-',label="With delay compensation")

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.axis('equal')
plt.show()
