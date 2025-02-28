import matplotlib.pyplot as plt
import math 

m = 0.1  # kg
xm = 0.05  # m
k = 20  # N/m
b = 0.1  # Ns/m
x = xm
v = 0
t = 0  # s
dt = 0.001  # s
w2 = math.sqrt(k/m)
time = []
theory_x_values = []
x_values = []

# Making variables for kinetic energy
kinetic_energy = []
# Making potential energy
potential_energy = []

while t < 4:
    a = -(k*x) / m
    v = v + a * dt
    x = x + v * dt
    t = t + dt
    time.append(t)
    x_values.append(x)
    theory_x = xm* math.cos(w2*t)
    theory_x_values.append(theory_x)
    # Kinetic energy
    kinetic_energy.append(0.5 * m * v**2)
    # Potential energy
    potential_energy.append(0.5 * k * x**2)

plt.plot(time, theory_x_values, 'r.', label='Theory')
plt.plot(time, x_values, 'b.', label='Simulation')
plt.plot(time, kinetic_energy, 'g.', label='Kinetic Energy')
plt.plot(time, potential_energy, 'y.', label='Potential Energy')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.title('Simple Harmonic Motion')
plt.legend()
plt.grid()
plt.show()