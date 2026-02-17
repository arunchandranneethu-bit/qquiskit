# Import required libraries
from qiskit import QuantumCircuit, Aer, execute
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a Quantum Circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard Gate (H)
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Use Aer simulator
simulator = Aer.get_backend('qasm_simulator')

# Execute the circuit
result = execute(qc, simulator, shots=1000).result()

# Get results
counts = result.get_counts(qc)

print("Measurement Results:", counts)

# Plot histogram
plot_histogram(counts)
plt.show()
