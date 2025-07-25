import random
import time

# Define CAN message types
CAN_MESSAGES = {
    0x101: 'RPM',
    0x102: 'Speed',
    0x103: 'Temperature',
    0x104: 'Fuel'
}

def encode_data(value):
    """Encodes a value into 8 bytes (little endian), padded with zeros."""
    byte_value = value.to_bytes(2, byteorder='little')
    return list(byte_value) + [0x00] * 6  # pad to 8 bytes

def generate_can_message():
    """Generates a random CAN message mimicking real vehicle telemetry."""
    can_id = random.choice(list(CAN_MESSAGES.keys()))
    signal_type = CAN_MESSAGES[can_id]

    if signal_type == 'RPM':
        value = random.randint(800, 3500)  # realistic RPM range
    elif signal_type == 'Speed':
        value = random.randint(0, 120)     # km/h
    elif signal_type == 'Temperature':
        value = random.randint(70, 110)    # degrees Celsius
    elif signal_type == 'Fuel':
        value = random.randint(5, 100)     # percentage

    return {
        'timestamp': time.time(),
        'can_id': hex(can_id),
        'signal': signal_type,
        'value': value,
        'data': encode_data(value)
    }

# Test mode
if __name__ == "__main__":
    while True:
        msg = generate_can_message()
        print(f"[{msg['timestamp']:.2f}] ID: {msg['can_id']} ({msg['signal']}) | Value: {msg['value']} | Data: {msg['data']}")
        time.sleep(0.5)


