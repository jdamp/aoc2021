import numpy as np

fish = np.loadtxt("input.txt", delimiter=",", dtype=np.int64)
initial_state, _ = np.histogram(fish, bins=np.arange(-0.5, 9.5, 1))
m_transition = np.array([
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0]
])

m80 = np.linalg.matrix_power(m_transition, 80)
result80 = m80@initial_state
print(f"After 80 days: {result80.sum()} fish")

m80_256 = np.linalg.matrix_power(m_transition, 256-80)
result256 = m80_256@result80
print(f"After 256 days: {result256.sum()} fish")