system_data = {
    "Device1" : {"room":"big", "heat":"high", "isactive":"on"},
    "Device2" : {"room":"smal", "heat":"low", "isactive":"on"},
    "Device3" : {"room":"smal", "heat":"high", "isactive":"off"}
}
# intertwined dictionaries in inner dictionaries you define them with : not =
device_ID = input("please enter device ID (key): ")
target_info = system_data.get(device_ID)  # if device id is not accurate this will return none
if target_info:
    print(f"{device_ID}'s heat:{target_info['heat']}")
    print(f"{device_ID}'s room:{target_info['room']}")
else:
    print("device could not found")
device_ID = input("please enter the device ID (key) that you want to change its heat condition: ")
target_info = system_data.get(device_ID)
if target_info:
    target_info["heat"] = input("please enter new heat condition: ")
    print(f"new heat:{target_info['heat']}")
else:
    print("device could not found")
added_device = input("please enter a new device: ")
r = input("please enter the rooms condition: ")
h = input("please enter the heat condition: ")
status = input("please enter the status condition: ")
system_data[added_device] = {"room":r, "heat":h, "isactive":status}
del_ID = input("Silmek istediğiniz cihaz ID: ")
if del_ID in system_data:
    removed_data = system_data.pop(del_ID) 
    print(f"{del_ID} deleted. deleted data: {removed_data}")
else:
    print("device could not found")
print("CURRENT INFORMATION")
for d_name, d_details in system_data.items():
    print(f"device name:{d_name}")
    for k, v in d_details.items():
        print(f"k:{k}|||v:{v}")