from matplotlib import pyplot as plt
import numpy as np
import sys

'''
	Scheme of simulation domain

	----------------------------> X
	0
'''

# Courant condition: c * dt < dx

c = 1450 # m/s - material parameter
u0 = 1 # initial u value
time = 0.035 # Total time in seconds
dt = 0.0004 # Time step in seconds
nt = int(time / dt) # Amount of time steps
lx = 200 # Length along X in meters
dx = 1 # Spatial step along X in meters
nx = int(lx / dx) # Number of nodes along X

# equation: du/dt + c * du/dx = 0
# node = [u]
# initial conditions
u = u0 * np.where(abs(np.linspace(-10, 10, nx)) <= 1, 1, 0)

# operator matrix
# u_m^(n+1) = u_m^n - c * dt / dx * (u_m^n - u_(m-1)^n)
A = np.eye(u.size) - np.roll(np.eye(u.size), -1, axis=1)

def save_results():
	fix, ax = plt.subplots(2, 1)
	ax[0].set_ylim(0, u0)
	ax[0].grid()
	ax[0].set_title('Initial profile')
	ax[0].plot(u0 * np.where(abs(np.linspace(-10, 10, nx)) <= 1, 1, 0)) # initial conditions
	ax[1].set_ylim(0, u0)
	ax[1].grid()
	ax[1].set_title('Final profile', pad = 0)
	ax[1].plot(u) # final profile
	plt.savefig('profile.png')

if __name__ == '__main__':
	# main time loop
	for n in range(nt):
		u = u - c * dt / dx * A @ u
	# save results
	save_results()
