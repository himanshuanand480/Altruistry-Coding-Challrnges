readings = list(map(int, input().split()))
def optimized_energy_monitoring(readings):
    if any(x < 10 or x > 200 for x in readings):
        print("INVALID INPUT")
        return
    sensor_sums = [0] * 5
    for i in range(20):
        sensor_sums[i % 5] += readings[i]  
    sensor_averg = [round(total / 4) for total in sensor_sums]
    max_avg = max(sensor_averg)
    if max_avg < 50:
        print("Energy consumption is optimal.")
    else:
        sensor_number = sensor_averg.index(max_avg) + 1
        print(f"Sensor Number : {sensor_number}")
optimized_energy_monitoring(readings)

#Time Complexity:O(N)
#Space Complexity:O(1)
