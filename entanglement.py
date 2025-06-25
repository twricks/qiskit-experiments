#Plotting the Von Neumann Entropy 
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector,random_statevector, DensityMatrix, partial_trace
from qiskit.primitives import StatevectorSampler
from qiskit.visualization import plot_bloch_vector, plot_histogram
import matplotlib.pyplot as plt
points = 100
MapArray = np.zeros((points,points))


for n in range (points):
    theta = n*(np.pi/50)
    for m in range (points):
        phi = m*(np.pi/50)
        comp1 = np.cos(theta/2)
        comp2 = np.exp(1j*phi)*np.sin(theta/2)
        qc = QuantumCircuit(2)
        qc.h(0) #put the first in an equal superposition state
        qc.initialize([comp1,comp2],1) #sets qubit state 2
        qc.cx(0,1) #CNOT
        final_state = Statevector.from_instruction(qc)
        rho = DensityMatrix(final_state)
        rho_1 = partial_trace(rho,[0]) #tracing out the first qubit
        eigvals = np.linalg.eigvalsh(rho_1.data)
        S = -np.sum([p * np.log2(p) for p in eigvals if p > 0])
        MapArray[n][m]=S



plt.imshow(MapArray, cmap='viridis', aspect='auto')
plt.colorbar(label='Value')

# Label the axes
plt.xlabel(r'$\phi$')
plt.ylabel(r'$\theta$')
plt.title(r'2-qubit entanglement as a function of $\theta$, $\phi$')

plt.show()