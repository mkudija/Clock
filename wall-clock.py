"""
Demo of a line plot on a polar axis.
"""
import numpy as np
import matplotlib.pyplot as plt


#r = np.arange(0, 3.0, 0.01)
#theta = 2 * np.pi * r

ax = plt.subplot(111, projection='polar')
#ax.text(0, 1, r'an equation: $E=mc^2$', fontsize=15)

numbers = range(0,24)
#numbers = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
rmax = 100
r = rmax*.85
l_dash = rmax*.08


# print outer numbers (24-hour)
idx = -np.pi/2
for number in range(0,len(numbers)):
	ax.text(idx,r,str(numbers[number]),ha='center',va='center',fontsize=15,weight='bold')
	idx -= 2*np.pi/len(numbers)

# print inner numbers (12-hr)
idx = np.pi/2 - 2*np.pi/len(numbers)
for number in numbers[1:13]:
	ax.text(idx,r*.89,str(numbers[number]),ha='center',va='center',weight='bold',color='red')
	idx -= 2*np.pi/len(numbers)


# print hour tick marks
idx = -np.pi/2
for number in range(0,len(numbers)):
	plt.plot([idx,idx],[rmax-l_dash,rmax],'-k')
	idx -= 2*np.pi/len(numbers)

# print half hour tick marks
idx = -np.pi/2 - (2*np.pi/len(numbers))/2
for number in range(0,len(numbers)):
	plt.plot([idx,idx],[rmax-l_dash/2,rmax],'-k')
	idx -= 2*np.pi/len(numbers)

# print 10 min tick marks
numbers_stick = range(0,24*6)
idx = -np.pi/2
for number in range(0,len(numbers_stick)):
	plt.plot([idx,idx],[rmax-l_dash/4,rmax],'-k')
	idx -= 2*np.pi/len(numbers_stick)	
# can make all ticks with this if we use "if" with right conditions





#-------------------------------------------------------------
city = 'Paso Robles, CA'

# DECEMBER
#--------------------------------------
sunrise_hr  = 7
sunrise_min = 8

sunset_hr  = 16
sunset_min = 52
#--------------------------------------

'''
#-------------------------------------------------------------
city = 'Columbus, OH'

# DECEMBER
#--------------------------------------
sunrise_hr  = 7
sunrise_min = 50

sunset_hr  = 17
sunset_min = 10
#--------------------------------------
'''

sunrise_hr_neg = sunrise_hr * -1
sunrise_min_neg  = sunrise_min * -1

hr_pi = sunrise_hr_neg * 2*np.pi/24 
hr_min = (hr_pi + sunrise_min_neg * 2*np.pi/(24*60) ) - np.pi/2

sunrise_time = sunrise_hr + sunrise_min/60
sunset_time  = sunset_hr  + sunset_min/60

night_time = 24 - (sunset_time - sunrise_time)
night_time_rad = night_time * 2*np.pi/24

angles = [hr_min,hr_min]
ax.bar(angles, np.full(2, 100), width=night_time_rad, bottom=0.0, color='#E5E3E2', linewidth=0)


# JUNE
#city = 'Paso Robles, CA'
#--------------------------------------
sunrise_hr  = 5
sunrise_min = 47

sunset_hr  = 20
sunset_min = 21
#--------------------------------------

'''
# JUNE
#city = 'Columbus, OH'
#--------------------------------------
sunrise_hr  = 6
sunrise_min = 3

sunset_hr  = 21
sunset_min = 3
#--------------------------------------
'''

sunrise_hr_neg = sunrise_hr * -1
sunrise_min_neg  = sunrise_min * -1

hr_pi = sunrise_hr_neg * 2*np.pi/24 
hr_min = (hr_pi + sunrise_min_neg * 2*np.pi/(24*60) ) - np.pi/2

sunrise_time = sunrise_hr + sunrise_min/60
sunset_time  = sunset_hr  + sunset_min/60

night_time = 24 - (sunset_time - sunrise_time)
night_time_rad = night_time * 2*np.pi/24

angles = [hr_min,hr_min]
ax.bar(angles, np.full(2, 100), width=night_time_rad, bottom=0.0, color='#959493', linewidth=0)



# print name and location
ax.text(90*(np.pi/180),20,city,ha='center',va='center',weight='bold',fontsize=8)

ax.set_rmax(rmax)
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)
ax.grid(False)

plt.savefig('clock-' + city + '.png', dpi=300)
plt.show()