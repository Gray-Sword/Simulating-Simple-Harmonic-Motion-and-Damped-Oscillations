import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

mass = 1.0
spring_constant = 1.0
damping_coefficient = 0.2

initial_position = 1.0
initial_velocity = 0.0

time_span = (0, 20)
time_eval = np.linspace(time_span[0], time_span[1], 500)

def damped_harmonic_oscillator(t, y):
    x, v = y
    dxdt = v
    dvdt = -(spring_constant / mass) * x - (damping_coefficient / mass) * v
    return [dxdt, dvdt]

initial_conditions = [initial_position, initial_velocity]

solution = solve_ivp(
    damped_harmonic_oscillator, 
    time_span, 
    initial_conditions, 
    t_eval=time_eval
)

plt.figure(figsize=(10, 6))
plt.plot(solution.t, solution.y[0], label="Position (x)")
plt.plot(solution.t, solution.y[1], label="Velocity (v)")
plt.title("Damped Harmonic Oscillator")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
