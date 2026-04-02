sensors = {"S1":"online", "S2":"offline", "S3":"online", "S4":"offline"}
sensors.update({input("please enter a sensor id(key): "):input("please enter a sensor condition (value): ")})
control = sensors.get(input("please enter the sensor id(key) that you want to look for: "), "sensor could not found")
print(control)
key_to_delete = input("please enter the sensor id that you want to delete: ")
deleted_condition = sensors.pop(key_to_delete, "could not found")
print(f"sensor : {key_to_delete} status: {deleted_condition} deleted")
for k, v in sensors.items():
    print(f"sensor:{k}----condition:{v}")

# NOTE pop function returns condition