import csv
import serial
import serial.tools.list_ports
import time

class read_sensor:
    def __init__(self, port_name, baud_rate=9600):
        self.port_name = port_name
        self.baud_rate = baud_rate
        self.ser = serial.Serial(self.port_name, self.baud_rate, timeout=1)
        self.file = open("value.csv", "w", newline="")
        self.rows = csv.DictWriter(self.file, fieldnames=["Servo", "Led_pwm", "Distance"])

        if self.ser.is_open:
            print(f"{self.port_name} has succesfully opened!")
            self.ser.reset_input_buffer()
            time.sleep(1)

    @property
    def port_name(self):
        return self._port_name

    @port_name.setter
    def port_name(self, port_name):
        if port_name is None:
            raise ValueError("Invalid port name")
        self._port_name = port_name

    @property
    def baud_rate(self):
        return self._baud_rate

    @baud_rate.setter
    def baud_rate(self, baud_rate):
        if baud_rate != 9600:
            raise ValueError("Invalid baud rate")
        self._baud_rate = baud_rate

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.ser.close()
        self.file.close()
        print(f"\n\n{self.port_name} has closed ----- System closed succesfully!\n\n")

    def _save_to_csv(self, servo, led, dist):
        self.file.seek(0)
        self.file.truncate()
        self.rows.writeheader()
        self.rows.writerow({"Servo": servo, "Led_pwm": led, "Distance": dist})
        self.file.flush()
        self.ser.reset_input_buffer()

    def _show_at_bar(self, device_value, maks_limit, division_limit):
        filled_section = int((min(device_value, maks_limit) * 20) / division_limit)
        bar = "█" * filled_section + "-" * (20 - filled_section)
        return bar


    def read_write_sensor(self):
        while True:
            try:
                if self.ser.in_waiting >= 7:
                    raw_bytes = self.ser.read(7)
                    if raw_bytes[0] == 0xAA and raw_bytes[1] == 0x55:
                        servo_value = raw_bytes[2]
                        led_pwm_value = (raw_bytes[3] << 8) | raw_bytes[4]
                        distance = (raw_bytes[5] << 8) | raw_bytes[6]
                        print(f"\nServo: {servo_value:3} |{self._show_at_bar(servo_value, 125, 115)}|")
                        print(f"Led_pwm: {led_pwm_value:3} |{self._show_at_bar(led_pwm_value, 1000, 960)}|")
                        print(f"Distance: {distance}")

                        self._save_to_csv(servo_value, led_pwm_value, distance)

            except serial.SerialException:
                print("\n\nERROR --- USB cable has probably been disconnected\n")
                print("Please control your USB cable\n\n")
                break

def port_selector():
    ports = serial.tools.list_ports.comports()
    if not ports:
        print("\n\nCould not fpund any ports...\n\n")
        return None

    for index, port in enumerate(ports):
        print(f"[{index + 1}] - {port.device} --- {port.description}\n")

    try:
        user_choice = int(input("Please enter the number of the port that you have chosen: "))
        selected_port = ports[user_choice - 1].device
        print(f"\n\n{selected_port} has chosen!\n\n")
        return selected_port
    except (ValueError, IndexError):
        print("\n\nCould not found the port that you have entered\n\n")
        return None


def main():
    try:
        with read_sensor(port_selector()) as reader:
            reader.read_write_sensor()
    except KeyboardInterrupt:
        print("\n\nSYSTEM CLOSED SUCCESFULLY --- system closed manually by user\n\n")
    except ValueError as error:
        print(f"\n\nSYSTEM CLOSED --- {error}\n\n")

if __name__ == "__main__":
    main()