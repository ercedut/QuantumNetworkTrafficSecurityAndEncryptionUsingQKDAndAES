QuantumSecureNet

Project Overview

QuantumSecureNet is a cutting-edge project focused on developing a secure communication framework that combines classical cryptography with quantum cryptography. This project leverages Quantum Key Distribution (QKD) using the BB84 protocol, 
AES encryption, and traffic obfuscation to ensure a robust and future-proof security system that can withstand both classical and quantum attacks.

Features

- Quantum Key Distribution (QKD): Implements the BB84 protocol to generate secure cryptographic keys based on quantum mechanics principles.
- AES Encryption: Uses AES (Advanced Encryption Standard) to encrypt sensitive data, with keys generated from the QKD process.
- Traffic Obfuscation: Introduces dummy packets to obfuscate real traffic, making it harder for attackers to perform traffic analysis.

## File Structure

- main.py: Main script that orchestrates the QKD, encryption, and traffic obfuscation.
- qkd.py: Contains the implementation of the BB84 Quantum Key Distribution protocol.
- encryption.py Handles AES encryption and decryption using the generated quantum keys.
- traffic_obfuscation.py: Generates dummy traffic packets and sends them with random delays to obfuscate communication.

## How to Run the Project

1. Clone the repository:

   git clone https://github.com/ercedut/QuantumNetworkTrafficSecurityAndEncryptionUsingQKDAndAES.git


2. Install the required dependencies:


   pip install -r requirements.txt


3. Run the main script:


   python3 main.py


Purpose

This project is designed to explore the combination of classical and quantum cryptographic techniques, with potential use in academic research, particularly in the context of a PhD project. It provides a hybrid approach to address the evolving security challenges posed by quantum computing.

