import serial
import time
import csv

ser = serial.Serial('COM3', 9600)


print("Here is your csv!\n\n")
with open("value.csv", "w", newline="") as file:
    headers = ["SERVO", "LED_PWM", "DISTANCE"]
    rows = csv.DictWriter(file, fieldnames=headers)
    
    if ser.is_open:
        print("COM3 has opened succesfully!\n")
        time.sleep(1)
        ser.reset_input_buffer() # İçerideki eski ve yarım kalmış baytları çöpe at

    try:
        while True:
            if ser.in_waiting >= 7:
                raw_bytes = ser.read(7)
                if raw_bytes[0] == 0xAA and raw_bytes[1] == 0x55:
                    servo_value = raw_bytes[2]
                    led_pwm_value = (raw_bytes[3] << 8) | raw_bytes[4]
                    distance = (raw_bytes[5] << 8) | raw_bytes[6]
                    print(f"servo value: {servo_value}")
                    print(f"LED PWM value: {led_pwm_value}")
                    print(f"distance: {distance}")

                    file.seek(0)  # imleci en başa (0 satıra aldık)
                    file.truncate()  # imleçten sonraki verilerin tümünü sil
                    rows.writeheader()
                    rows.writerow({"SERVO": servo_value, "LED_PWM": led_pwm_value, "DISTANCE": distance})
                    file.flush()  # dosyayı RAM de bekletme doğrudan CSV ye yazdır
                    ser.reset_input_buffer()
                    time.sleep(0.05)

    except KeyboardInterrupt:
        ser.close()
        print("PORT has closed...")