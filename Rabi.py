#qiskit 1.4.2- qiskit.pulse dependency problems not resolved in 2.0 as of June 2025. 
import numpy as np
import cmath
from qiskit.quantum_info import Operator
from qiskit_dynamics import Solver, Signal
from qiskit.quantum_info.states import Statevector
from qiskit.quantum_info import DensityMatrix
from qiskit.visualization import plot_bloch_vector
import matplotlib.pyplot as plt

#qubit driven at reasonance
v_z = 1
v_x = 1
v_d = 0 

#Importing Pauli matrices
X = Operator.from_label('X')
Y = Operator.from_label('Y')
Z = Operator.from_label('Z')

#specifying the solver used
solver = Solver(
    static_hamiltonian=.5 * 2 * np.pi * v_z * Z,
    hamiltonian_operators=[2 * np.pi * v_x * X],
)

t_final = 1.0 / v_x
tau = .005

#specifying initial state
y0 = Statevector([1., 0.])

n_steps = int(np.ceil(t_final / tau)) + 1
t_eval = np.linspace(0., t_final, n_steps)
signals = [Signal(envelope=1., carrier_freq=v_d)]

#solving for specified initial state
sol = solver.solve(t_span=[0., t_final], y0=y0, signals=signals, t_eval=t_eval)

fontsize = 16

#collecting times, solutions from the Statevector object returned by the solver
times = sol.t
probs = [abs(state.data[0])**2 for state in sol.y]

plt.figure(figsize=(8, 5))
plt.plot(times, probs, label='P(|0⟩)')
plt.xlabel('Time')
plt.ylabel('Occupation Probability')
plt.title('Occupation Probability of |0⟩ Over Time')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

