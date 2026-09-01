import csv
import serial
import time

class Read_Sensor:
    def __init__(self, port_name, baud_rate=9600):
        self.ser = serial.Serial(port_name, baud_rate)
        self.file = open('value.csv', 'w', newline="")
        self.rows = csv.DictWriter(self.file, fieldnames=["SERVO", "LED_PWM", "DISTANCE"])
        self.port_name = port_name  # bu sayede class daki farklı fonksiyonlarda bu variable ı kullanbileceğim

        if self.ser.is_open:
            print(f"{port_name} has opened!\n\n")
            time.sleep(1)
            self.ser.reset_input_buffer()  # içerdeki eski verileri sildik

    def write_and_read_values(self):
        print("Values are writing to the CSV file...\n\n")
        try:
            while True:
                if self.ser.in_waiting >= 7:
                    raw_bytes = self.ser.read(7)
                    if raw_bytes[0] == 0xAA and raw_bytes[1] == 0x55:
                        servo_value = raw_bytes[2]
                        led_pwm_value = (raw_bytes[3] << 8) | raw_bytes[4]
                        distance = (raw_bytes[5] << 8) | raw_bytes[6]
                        print(f"servo value: {servo_value}")
                        print(f"LED PWM value: {led_pwm_value}")
                        print(f"distance: {distance}")

                        self.file.seek(0)
                        self.file.truncate()
                        self.rows.writeheader()
                        self.rows.writerow({"SERVO": servo_value, "LED_PWM": led_pwm_value, "DISTANCE": distance})
                        self.file.flush()
                        self.ser.reset_input_buffer()
                        time.sleep(0.05)

        except KeyboardInterrupt:
            self.close_system()

    def close_system(self):
        self.ser.close()
        self.file.close()
        print(f"{self.port_name} has closed!\n\n") 
         # port_name başka fonksiyonda tanımlandığı için bunun içine tanımlayamıyordum ama __init__ e yazdığım sayesinde tanımlanabilir

def main():
    reader = Read_Sensor('COM3')
    reader.write_and_read_values()

if __name__ == "__main__":
    main()