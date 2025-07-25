import csv
import ast

# Decoder function
def decode_can_message(can_id, data_bytes):
    decoded = {}

    if can_id == '0x101':
        rpm = (data_bytes[0] << 8 | data_bytes[1]) / 4
        decoded['Engine RPM'] = round(rpm, 2)

    elif can_id == '0x102':
        speed = data_bytes[0]
        decoded['Speed (km/h)'] = speed

    elif can_id == '0x103':
        temp = data_bytes[0] - 40
        decoded['Engine Temp (°C)'] = temp

    elif can_id == '0x104':
        throttle = data_bytes[0] * 100 / 255
        decoded['Throttle Position (%)'] = round(throttle, 2)

    return decoded

# Read from logged CSV and decode
def decode_log(logfile="can_log.csv"):
    with open(logfile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            can_id = row['CAN_ID']
            data = ast.literal_eval(row['Data'])  # Convert string to list
            decoded = decode_can_message(can_id, data)
            if decoded:
                print(f"ID {can_id} | {decoded}")

if __name__ == "__main__":
    decode_log()
