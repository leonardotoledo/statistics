import matplotlib.pyplot as plt

def mma_value(vector, alpha, i):

	if i == 0:
		return vector[i]
	if i > 0:
		return alpha * vector[i] + (1-alpha) * mma_value(vector, alpha, i-1)

def mma(vector, N):

	averaged_values = []

	alpha = 1./N

	for i in range(len(vector)):

		averaged_values.append(mma_value(vector, alpha, i))

	return averaged_values


vector = [58.28, 57.96, 57.6, 58.03, 56.85, 57.77, 57.21]
time = range(1,8)

fig, ax = plt.subplots()
ax.plot(time, vector, label = 'original')
ax.plot(time, mma(vector, 1), '--', label = '1')
ax.plot(time, mma(vector, 2), '--', label = '2')
ax.plot(time, mma(vector, 3), '--', label = '3')
plt.legend()
plt.show()
