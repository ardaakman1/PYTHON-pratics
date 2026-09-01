import serial

ser = serial.Serial('COM3', 9600)

while True:
    if ser.in_waiting >= 2:  # en az 2 byte birikmesini bekledik
        raw_bytes = ser.read(2)
        high_byte = raw_bytes[0]
        low_byte = raw_bytes[1]
        distance = (high_byte << 8) | low_byte  # burada high ı 8 sola kaydırdık ve low ile veya ile birleştirdik
        print(f"distance: {distance}")