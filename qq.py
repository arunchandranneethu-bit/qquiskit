from qiskit import QuantumCircuit
from qiskit_aer import Aer
from qiskit import transpile

# Create circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate (creates superposition)
qc.h(0)

# Measure the qubit
qc.measure(0, 0)

# Use simulator
simulator = Aer.get_backend('aer_simulator')

# Compile and run
compiled_circuit = transpile(qc, simulator)
job = simulator.run(compiled_circuit, shots=1000)
result = job.result()

# Print results
counts = result.get_counts()
print("Measurement Results:", counts)
