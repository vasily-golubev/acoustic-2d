'''
	Scheme of simulation domain

	^ Y
	|
	---------------------------
	|                         |
	|                         |
	|                         |
	|                         |
	|                         |
	|                         |
	|                         |
	----------------------------> X
	(0,0)
'''

time = 1 # Total time in seconds
dt = 0.01 # Time step in seconds
nt = int(time / dt) # Amount of time steps
lx = 1 # Length along X in meters
ly = 1 # Length along Y in meters
dx = 0.1 # Spatial step along X in meters
dy = 0.1 # Spatial step along Y in meters
nx = int(lx / dx) # Number of nodes along X
ny = int(ly / dy) # Number of nodes along Y

# node = [vx, vy, p]

data_curr = [[0, 0, 0] * ny for _ in range(nx)] # n-th time layer data
data_next = [[0, 0, 0] * ny for _ in range(nx)] # (n+1)-th time layer data

def apply_initial_data():
	pass

def save_data():
	pass

if __name__ == '__main__':
	# initial conditions
	apply_initial_data()
	# main time loop
	for n in range(nt):
		# stepX
		for j in range(1, ny - 1): # Don't think much about boundaries
			for i in range(1, nx - 1):
				data_next[j][i] = data_curr[j][i] # FIXME
		# stepY
		for i in range(1, nx - 1): # Don't think much about boundaries
			for j in range(1, ny - 1):
				data_next[j][i] = data_curr[j][i] # FIXME
		# update time layer
		for j in range(1, ny - 1): # Don't think much about boundaries
			for i in range(1, nx - 1):
				data_curr[j][i] = data_next[j][i]
	# save results
	save_data();
