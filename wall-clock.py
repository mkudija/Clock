import numpy as np
import matplotlib.pyplot as plt

# set up plot and define constants
ax = plt.subplot(111, projection='polar')
numbers = range(0,24)
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


def plot_night(sunrise_hr, sunrise_min, sunset_hr, sunset_min, color):
	sunrise_hr_neg = sunrise_hr * -1
	sunrise_min_neg  = sunrise_min * -1

	hr_pi = sunrise_hr_neg * 2*np.pi/24 
	hr_min = (hr_pi + sunrise_min_neg * 2*np.pi/(24*60) ) - np.pi/2

	sunrise_time = sunrise_hr + sunrise_min/60
	sunset_time  = sunset_hr  + sunset_min/60

	night_time = 24 - (sunset_time - sunrise_time)
	night_time_rad = night_time * 2*np.pi/24

	ax.bar(hr_min, rmax, width=night_time_rad, bottom=0.0, color=color, linewidth=0)


def plot_city(sunrise_dec, sunset_dec, sunrise_jun, sunset_jun, city):
	plot_night(sunrise_dec[0], sunrise_dec[1], sunset_dec[0], sunset_dec[1], color='#E5E3E2')
	plot_night(sunrise_jun[0], sunrise_jun[1], sunset_jun[0], sunset_jun[1], color='#959493')

	# print name and location
	ax.text(90*(np.pi/180),20,city,ha='center',va='center',weight='bold',fontsize=8)

	ax.set_rmax(rmax)
	ax.axes.get_xaxis().set_visible(False)
	ax.axes.get_yaxis().set_visible(False)
	ax.grid(False)

	plt.savefig('clock-' + city + '.png', dpi=500)
	plt.show()

'''
city = 'Columbus, OH'
sunrise_dec = [7, 50]
sunset_dec  = [17, 10]
sunrise_jun = [6, 3]
sunset_jun  = [21, 3]

'''
city = 'Paso Robles, CA'
sunrise_dec = [7, 8]
sunset_dec  = [16, 52]
sunrise_jun = [5, 47]
sunset_jun  = [20, 21]


plot_city(sunrise_dec, sunset_dec, sunrise_jun, sunset_jun, city)
