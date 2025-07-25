import time
import csv
from cansimulator import generate_can_message  # Reuse simulator

def log_can_message(logfile="can_log.csv", duration=10):
    print(f"Logging CAN messages for {duration} seconds...")
    start_time = time.time()

    # Open CSV log file
    with open(logfile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Timestamp', 'CAN_ID', 'Data'])

        while time.time() - start_time < duration:
            msg = generate_can_message()
            writer.writerow([f"{msg['timestamp']:.2f}", msg['can_id'], msg['data']])
            print(f"Logged: {msg['can_id']} -> {msg['data']}")
            time.sleep(0.5)

    print(f"✅ Logging complete. Saved to '{logfile}'.")

if __name__ == "__main__":
    log_can_message()
