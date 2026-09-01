import csv
import serial
import serial.tools.list_ports
import time

# burada kod daha modüler hale geldi OOP gelişti artık port name de kontrol ediliyor ve terminal üzerinde port seçiliyor

class read_sensor:
    def __init__(self, port_name, baud_rate=9600):
        self.port_name = port_name
        self.baud_rate = baud_rate
        self.ser = serial.Serial(self.port_name, self.baud_rate)
        self.file = open("value.csv", "w", newline="")
        self.rows = csv.DictWriter(self.file, fieldnames=["Servo", "Led_pwm", "Distance"])
      
        if self.ser.is_open:
            print(f"{port_name} has opened!\n\n")
            time.sleep(1)
            self.ser.reset_input_buffer()

    @property
    def baud_rate(self):
        return self._baud_rate

    @baud_rate.setter
    def baud_rate(self, baud_rate):
        if baud_rate != 9600:
            raise ValueError('Invalid baud rate!\n')
        self._baud_rate = baud_rate

    @property   # yenilik
    def port_name(self):
        return self._port_name

    @port_name.setter
    def port_name(self, port_name):
        if port_name is None:  # burda is kullanıldı == yerine çünkü == değere bakar is ise bellek adresine gidip bakar
            raise ValueError('Invalid port name!\n')
        self._port_name = port_name

    def read_write_sensor(self):
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
                        self.rows.writerow({"Servo": servo_value, "Led_pwm": led_pwm_value, "Distance": distance})
                        self.file.flush()
                        self.ser.reset_input_buffer()
                        time.sleep(0.1)

        except KeyboardInterrupt:
            self.close_system()

    def close_system(self):
        self.file.close()
        self.ser.close()
        print(f"{self.port_name} has closed!\n\n")


def port_selector():
    ports = serial.tools.list_ports.comports()  # bilgisayara takılı olan tüm portları listeye alır

    if not ports:
        print("Could not found any serial device!\n")
        return None

    print("Current ports have found!\n")
    for index, port in enumerate(ports):  # enumarate() ile numaralandırdık
        print(f"[{index + 1}] - {port.device}: {port.description}") # port.device portun kısa adı (COM3)
        #  port.description portun windows taki tam adı (USB universal serial bus)

    try:
        user_choice = int(input("Please enter the number of the port that you have chosen: "))
        selected_port = ports[user_choice - 1].device
        print(f"{selected_port} has chosen!\n\n")
        return selected_port
    except (IndexError, ValueError):  #
        print("The port that you entered could not found...\n\n")
        return None
    
def main():
    try:
        reader = read_sensor(port_selector())
        reader.read_write_sensor()
    except ValueError as error:  # obje hata döndürürse buna girsin
        print(f"\n\nSYSTEM STOPPED: {error}\n")

if "__main__" == __name__:
    main()