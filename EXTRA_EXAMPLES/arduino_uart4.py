import csv
import time
import serial

class read_sensor:
    def __init__(self, port_name, baud_rate=9600):
        self.ser = serial.Serial(port_name, baud_rate)
        self.file = open("value.csv", "w", newline="")
        self.rows = csv.DictWriter(self.file, fieldnames=["Servo", "led_pwm", "distance"])
        self.port_name = port_name
        self.baud_rate = baud_rate

        if self.ser.is_open:
            print(f"{port_name} has opened!\n\n")
            time.sleep(1)
            self.ser.reset_input_buffer()

    @property
    def baud_rate(self):
        return self._baud_rate

    @baud_rate.setter  # property tanımlamadan setter tanımlayamayız ve setter güvenlik önlemi
    def baud_rate(self, baud_rate):  # yani bir yazılmcı veya kullanıcı baudrate i 9600 girerse program çökecek
        if baud_rate != 9600:
            raise ValueError('Invaild Baud rate!\n')
        # return self._baud_rate setter fonksiyonlar değer return etmez atama yaparlar
        self._baud_rate = baud_rate

    def read_write_sensor(self):
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

                        self.file.seek(0)  # imleci 0 a (ilk satır ilk sütun) götür
                        self.file.truncate()
                        self.rows.writeheader()
                        self.rows.writerow({"Servo": servo_value, "led_pwm": led_pwm_value, "distance": distance})
                        self.file.flush()
                        self.ser.reset_input_buffer()
                        time.sleep(0.05)

        except KeyboardInterrupt:
            self.close_system()  # burada neden self.close_system demeliyim neden close_system desem olmaz?
            # çünkü close_system de def main de olduğu gibi globade fonksiyonu arar self diyerek bu objede bakmasını sağlarız

    def close_system(self):
        self.file.close()
        self.ser.close()
        print(f"{self.port_name} has closed!\n\n")  # burada neden self.port_name oldu neden port_name değil sadece
        # çünkü port_name sadece bir parametre ve __init__ fonkisyonu bittiği zaman siliniyor self.port_name gerçek değişken

def main():
    reader = read_sensor('COM3')
    reader.read_write_sensor()  # method u çalıştırdım

if "__main__" == __name__:
    main()