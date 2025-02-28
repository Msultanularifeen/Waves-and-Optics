import matplotlib.pyplot as plt

# Time parameters
total_time = 20 # seconds
dt = 0.1  # time step in seconds

# Car parameters
acceleration_phase_duration = 5  # seconds
constant_speed_phase_duration = 10  # seconds
deceleration_phase_duration = 5  # seconds
max_speed = 30  # m/s

# Lists to store values
time_values = []
velocity_values = []
speed_values = []
acceleration_values = []

# Simulation
t = 0
v = 0
while t < total_time:
    if t < acceleration_phase_duration:
        a = max_speed / acceleration_phase_duration
    elif t < acceleration_phase_duration + constant_speed_phase_duration:
        a = 0
    else:
        a = -max_speed / deceleration_phase_duration
    
    v = v + a * dt
    t = t + dt
    
    time_values.append(t)
    velocity_values.append(v)
    speed_values.append(abs(v))
    acceleration_values.append(a)

# Plotting the graphs
plt.plot(time_values, velocity_values, 'r-', label='Velocity')
plt.plot(time_values, speed_values, 'b-', label='Speed')
plt.plot(time_values, acceleration_values, 'g-', label='Acceleration')
plt.xlabel('Time (s)')
plt.ylabel('Value')
plt.title('Car Velocity, Speed, and Acceleration over Time')
plt.legend()
plt.grid()
plt.show()