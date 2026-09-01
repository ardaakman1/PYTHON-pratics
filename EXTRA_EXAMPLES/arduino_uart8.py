import csv
import serial
import serial.tools.list_ports
import time

class read_sensor:
    def __init__(self, port_name, baud_rate=9600):
        self.port_name = port_name
        self.baud_rate = baud_rate
        self.ser = serial.Serial(self.port_name, self.baud_rate)
        self.file = open("value.csv", "w", newline="")
        self.rows = csv.DictWriter(self.file, fieldnames=["Servo", "Led_pwm", "Distance"])

        if self.ser.is_open:
            print(f"{self.port_name} has opened!\n")
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
        print(f"\n\n{self.port_name} has closed! --- system closed succesfully!\n\n")

    def _save_to_csv(self, servo, led, dist):
        self.file.seek(0)
        self.file.truncate()
        self.rows.writeheader()
        self.rows.writerow({"Servo": servo, "Led_pwm": led, "Distance": dist})
        self.file.flush()
        self.ser.reset_input_buffer()

    def read_write_sensor(self):
        while True:
            try:
                if self.ser.in_waiting >= 7:
                    raw_bytes = self.ser.read(7)
                    if raw_bytes[0] == 0xAA and raw_bytes[1] == 0x55:
                        servo_value = raw_bytes[2]
                        led_pwm_value = (raw_bytes[3] << 8) | raw_bytes[4]
                        distance = (raw_bytes[5] << 8) | raw_bytes[6]
                        print(f"Servo: {servo_value}\n")
                        print(f"Led_pwm: {led_pwm_value}\n")
                        print(f"Distance: {distance}\n")

                        self._save_to_csv(servo_value, led_pwm_value, distance)
            except serial.SerialException:  # wğwe while okunurken kablo çıkarsa
                print("\n\nERROR --- USB cable has probably been disconnected\n")
                print("Please control your USB cable\n\n")
                break  # dögüden çıkıp __exit__ a gitti

def port_selector():
    ports = serial.tools.list_ports.comports()
    if ports is None:
        print("\n\nCould not found any ports...\n\n")
        return None

    for index, port in enumerate(ports):
        print(f"[{index + 1}] - {port.device} --- {port.description}\n")

    try:
        user_choice = int(input("Please enter the number of the port that you have chosen: "))
        selected_port = ports[user_choice - 1].device
        print(f"{selected_port} has selected\n")
        return selected_port
    except (ValueError, IndexError):
        print("Could not found the port you have entered\n")
        return None

def main():
    try:
        with read_sensor(port_selector()) as reader:
            reader.read_write_sensor()
    except KeyboardInterrupt:
        print("\n\nSYSTEM CLOSED SUCCESFULLY --- system closed manually by user\n\n")
    except ValueError as error:
        print(f"\n\nSYSTEM CLOSED --- {error}\n\n")

if "__main__" == __name__:
    main() 
