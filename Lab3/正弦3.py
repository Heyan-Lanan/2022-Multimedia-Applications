import numpy as np
import matplotlib.pyplot as plt

a1 = np.random.rand(1)
a2 = np.random.rand(1)
a3 = np.random.rand(1)
w1 = np.random.rand(1)
w2 = np.random.rand(1)
w3 = np.random.rand(1)

x = np.arange(0, 300 * np.pi, 0.02)
y1 = a1 * np.sin(x + w1)
y2 = a2 * np.sin(2*x + w2)
y3 = a3 * np.sin(3*x + w3)
y = y1 + y2 + y3
y_frequency_1 = a1 * np.sin(0.5 * x + w1) + a2 * np.sin(x + w2) + a3 * np.sin(1.5 * x + w3)
y_frequency_2 = a1 * np.sin(2 * x + w1) + a2 * np.sin(4 * x + w2) + a3 * np.sin(6 * x + w3)
y_amplitude_1 = 0.5 * y
y_amplitude_2 = 2 * y

with open('test.txt', 'w') as write_f:
    write_f.write('[ASCII 44100Hz, Channels: 1, Samples: 62156, Flags: 0]' + '\n')
    for item in y:
        write_f.write(str(item) + '\n')

with open('test_frequency_1.txt', 'w') as write_f:
    write_f.write('[ASCII 44100Hz, Channels: 1, Samples: 62156, Flags: 0]' + '\n')
    for item in y_frequency_1:
        write_f.write(str(item) + '\n')

with open('test_frequency_2.txt', 'w') as write_f:
    write_f.write('[ASCII 44100Hz, Channels: 1, Samples: 62156, Flags: 0]' + '\n')
    for item in y_frequency_2:
        write_f.write(str(item) + '\n')

with open('test_amplitude_1.txt', 'w') as write_f:
    write_f.write('[ASCII 44100Hz, Channels: 1, Samples: 62156, Flags: 0]' + '\n')
    for item in y_amplitude_1:
        write_f.write(str(item) + '\n')

with open('test_amplitude_2.txt', 'w') as write_f:
    write_f.write('[ASCII 44100Hz, Channels: 1, Samples: 62156, Flags: 0]' + '\n')
    for item in y_amplitude_2:
        write_f.write(str(item) + '\n')

plt.plot(x, y1)
plt.show()
plt.plot(x, y2)
plt.show()
plt.plot(x, y3)
plt.show()
plt.plot(x, y1+y2+y3)
plt.show()
