import numpy as np
import matplotlib.pyplot as plot

time = np.arange(0, 10, 0.1); #get x value of the wave
amplitude = np.sin(time)


plot.plot(time, amplitude)# plot a sine wave using and amplitude obtained for the sine wave
plot.title('sine wave')#give a title for the sine wave plot

plot.xlabel('Time')

plot.ylabel('Amplitude = sin(time)')

plot.grid(True, which ='both')
plot.axhline(y=0, color='k')
plot.show()

#source: