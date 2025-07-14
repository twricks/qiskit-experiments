#quantum circuit to perform addition mod 4
#Qiskit version 1.4.2
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
import matplotlib.pyplot as plt
qc = QuantumCircuit(4) # initializes four qubits
qc.initialize([0,1],0)
qc.initialize([0,1],1) #Put qubits 1 & 2 in |1>, making their joint state,
#2-bit 'x' |1>|1>, which is 3.
qc.initialize([1,0],2) #put qubit 3, the first bit of y, into |0>
qc.initialize([0,1],3) #put qubit 4, the second bit of y, making
#their joint state |0>|1>, which is 1. we'll subject these four qubits to
#a series of operations that outputs a new 4-qubit, 2-bit state |3>|0>,
x_y_inputs = Statevector.from_instruction(qc)
print(x_y_inputs)
qc.ccx(1,3,2)#controlled-not on qubit 3, dependent on qubits 2 and 4.
qc.cx(0,2) #apply a CNOT to qubit 3 subject to state of qubit 1.
qc.cx(1,3) #apply a CNOT to qubit 4 subject to state of qubit 2.


output = Statevector.from_instruction(qc)
for i, amp in enumerate(output.data):
    if np.abs(amp) > 1e-6:  # filter out near-zero values
        bitstring = format(i, f'0{output.num_qubits}b')  # binary string of basis state
        print(f"|{bitstring}⟩ : amplitude = {amp.real:.3f}{amp.imag:+.3f}j")
qc.draw(output = 'mpl')
plt.show()
#print(output)

