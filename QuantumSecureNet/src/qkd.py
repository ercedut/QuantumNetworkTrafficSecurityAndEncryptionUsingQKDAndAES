from qiskit import QuantumCircuit, Aer, execute
import numpy as np

def bb84_key_generation(num_bits=128):
    alice_bits = np.random.randint(2, size=num_bits)
    alice_bases = np.random.randint(2, size=num_bits)

    quantum_circuits = []
    for bit, base in zip(alice_bits, alice_bases):
        qc = QuantumCircuit(1, 1)
        if base == 0:
            if bit == 1:
                qc.x(0)
        else:
            if bit == 1:
                qc.x(0)
            qc.h(0)
        quantum_circuits.append(qc)

    simulator = Aer.get_backend('qasm_simulator')
    results = []
    for qc in quantum_circuits:
        qc.measure(0, 0)
        result = execute(qc, simulator, shots=1).result()
        counts = result.get_counts()
        measured_bit = int(max(counts, key=counts.get))
        results.append(measured_bit)

    bob_bases = np.random.randint(2, size=num_bits)
    key = []
    for alice_bit, alice_base, bob_base, measured_bit in zip(alice_bits, alice_bases, bob_bases, results):
        if alice_base == bob_base:
            key.append(measured_bit)

    return ''.join(map(str, key))

if __name__ == "__main__":
    key = bb84_key_generation(128)
    print(f"Generated Quantum Key: {key}")
