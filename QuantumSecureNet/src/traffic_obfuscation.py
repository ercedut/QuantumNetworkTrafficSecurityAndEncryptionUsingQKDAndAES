import random
import time

def generate_dummy_packets(real_packets, num_dummy=10):
    dummy_packets = [f"DummyPacket-{i}" for i in range(num_dummy)]
    all_packets = real_packets + dummy_packets
    random.shuffle(all_packets)
    return all_packets

def send_packets_with_random_delay(packets, min_delay=0.1, max_delay=1.0):
    for packet in packets:
        delay = random.uniform(min_delay, max_delay)
        print(f"Sending packet: {packet} with delay {delay:.2f}s")
        time.sleep(delay)

if __name__ == "__main__":
    real_packets = [f"RealPacket-{i}" for i in range(5)]
    obfuscated_packets = generate_dummy_packets(real_packets, num_dummy=10)
    send_packets_with_random_delay(obfuscated_packets)
