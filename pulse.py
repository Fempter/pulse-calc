import numpy as np
import scipy.integrate

with open("pulse_b4_sport.txt", "r") as file1:
    data1 = [x.strip('\n').split(' ') for x in file1.readlines()]
    p1 = []
    for i,dane1 in enumerate(data1):
        time1, pulse1 = dane1
        if float(pulse1) > 0:
            p1.append(float(pulse1))

with open("pulse_after_sport.txt", "r") as file2:
    data2 = [x.strip('\n').split(' ') for x in file2.readlines()]
    p2 = []
    for i,dane2 in enumerate(data2):
        time2, pulse2 = dane2
        if float(pulse2) > 0:
            p2.append(float(pulse2))
        
p1_mean = np.mean(p1)
#print '\n',p1_mean

pp=[]
for i in p2:
    z = i - p1_mean
    pp.append(float(z))

time = np.arange(1,180.5,0.5)

#for i in time:
#    print i

print scipy.integrate.simps(pp, dx=0.5)
#print scipy.integrate.simps(pp,x=time)

with open("integral_data.txt", "w") as file_out:
    for i,pulse in enumerate(pp):
        count_pulse = pulse
        file_out.write('%f %f\n' % (i+0.5,count_pulse))