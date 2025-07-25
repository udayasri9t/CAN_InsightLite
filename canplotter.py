import csv
import ast
import matplotlib.pyplot as plt
from candecoder import decode_can_message

def load_and_plot(logfile="can_log.csv"):
    timestamps = []
    rpm_vals = []
    speed_vals = []
    temp_vals = []
    throttle_vals = []

    with open(logfile, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            ts = float(row['Timestamp'])
            can_id = row['CAN_ID']
            data = ast.literal_eval(row['Data'])

            decoded = decode_can_message(can_id, data)
            if not decoded:
                continue

            timestamps.append(ts)
            rpm_vals.append(decoded.get('Engine RPM'))
            speed_vals.append(decoded.get('Speed (km/h)'))
            temp_vals.append(decoded.get('Engine Temp (°C)'))
            throttle_vals.append(decoded.get('Throttle Position (%)'))

    # Remove None values and align timestamps
    def clean(x): return [v if v is not None else None for v in x]

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.plot(timestamps, clean(rpm_vals), 'r', label='RPM')
    plt.title('Engine RPM')
    plt.xlabel('Time'); plt.ylabel('RPM')
    plt.grid(); plt.legend()

    plt.subplot(2, 2, 2)
    plt.plot(timestamps, clean(speed_vals), 'g', label='Speed')
    plt.title('Vehicle Speed')
    plt.xlabel('Time'); plt.ylabel('km/h')
    plt.grid(); plt.legend()

    plt.subplot(2, 2, 3)
    plt.plot(timestamps, clean(temp_vals), 'b', label='Temp')
    plt.title('Engine Temp')
    plt.xlabel('Time'); plt.ylabel('°C')
    plt.grid(); plt.legend()

    plt.subplot(2, 2, 4)
    plt.plot(timestamps, clean(throttle_vals), 'm', label='Throttle')
    plt.title('Throttle %')
    plt.xlabel('Time'); plt.ylabel('%')
    plt.grid(); plt.legend()

    plt.tight_layout()
    plt.suptitle("CAN Bus Signal Visualization", fontsize=16, y=1.03)
    plt.show()

if __name__ == "__main__":
    load_and_plot()
