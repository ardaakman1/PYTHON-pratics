sensor_readings = [
    (1, 22.5, "OK"),
    (2, 45.0, "ALERT"),
    (3, 18.2, "OK"),
    (4, 55.3, "ALERT")
]
count = 0
for id, temp, condition in sensor_readings:
    if condition == "ALERT":
        print(f"sensor {id} has a high tempreture! {temp}")
    count += temp
average = count / len(sensor_readings)
print(f"the average tempreture is {average:.2f}!")