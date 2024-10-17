from qiskit import QuantumCircuit, Aer, execute
import numpy as np

def bb84_key_generation(num_bits=128):
    alice_bits = np.random.randint(2, size=num_bits)
    alice_bases = np.random.randint(2, size=num_bits)
    bob_bases = np.random.randint(2, size=num_bits)
    bob_results = []
    simulator = Aer.get_backend('qasm_simulator')

    for i in range(num_bits):
        qc = QuantumCircuit(1, 1)
        if alice_bases[i] == 0:
            if alice_bits[i] == 1:
                qc.x(0)
        else:
            if alice_bits[i] == 1:
                qc.x(0)
            qc.h(0)
        if bob_bases[i] == 1:
            qc.h(0)
        qc.measure(0, 0)
        result = execute(qc, simulator, shots=1, memory=True).result()
        measured_bit = int(result.get_memory()[0])
        bob_results.append(measured_bit)

    key = []
    for i in range(num_bits):
        if alice_bases[i] == bob_bases[i]:
            key.append(alice_bits[i])

    return ''.join(map(str, key))

if __name__ == "__main__":
    key = bb84_key_generation(128)
    print(f"Generated Quantum Key: {key}")
