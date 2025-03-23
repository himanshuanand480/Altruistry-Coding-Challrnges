readings = list(map(int, input().split()))
def brute_force_energy_monitoring(readings):
    if any(x < 10 or x > 200 for x in readings):
        print("INVALID INPUT")
        return
    sensors = [readings[i::5] for i in range(5)]
    avg = [round(sum(sensor) / 4) for sensor in sensors]
    max_avg = max(avg)

    if max_avg < 50:
        print("Energy consumption is optimal.")
    else:
        sensor_number = avg.index(max_avg) + 1
        print(f"Sensor Number : {sensor_number}")
brute_force_energy_monitoring(readings)

#Time Complexity:O(N)
#Space Complexity:O(N)
