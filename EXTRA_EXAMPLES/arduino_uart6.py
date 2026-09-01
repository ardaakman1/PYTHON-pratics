import csv
import serial
import serial.tools.list_ports
import time

# eğer program çalışıorken kablo koparsa veya 0 a bölme gibi bir hata gelirse hata almadan (kırmızı yazı olmadan) istediğimz şekilde ve daha güvenli bir halde programı kapatmayı sağlamak için kod geliştirildi

class read_sensor:
    def __init__(self, port_name, baud_rate=9600):
        self.port_name = port_name
        self.baud_rate = baud_rate
        self.ser = serial.Serial(self.port_name, self.baud_rate)
        self.file = open("value.csv",  "w", newline="")
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
            raise ValueError("Invalid port name!\n")
        self._port_name = port_name

    @property
    def baud_rate(self):
        return self._baud_rate

    @baud_rate.setter
    def baud_rate(self, baud_rate):
        if baud_rate != 9600:
            raise ValueError("Invalid baud rate\n")
        self._baud_rate = baud_rate

    def __enter__(self):
        return self  # with bloğu başladığında objeyi dışarı (as reader kısmına gönder)

    def __exit__(self, exc_type, exc_val, exc_tb):
        # kod nasıl biterse bitsin burası çalışıp kapanacak eski koddaki close_system() in daha güvenli hali gibi
        self.file.close()
        self.ser.close()
        print(f"{self.port_name} has closed / system is closed safely!\n")

    def read_write_sensor(self):  # artık burada try except yapmaya gerek yok çünkü program kapanırsa __exit_- ın içine girecek
        while True:
            try:  # bir tek while içindeyken biri USB yi çekerse o zaman program çöker çünkü ser.read() çalışamayabilir
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
            except serial.SerialException:
                print("\n\nERROR --- USB cable has probably been disconnected\n")
                print("Please control your USB cable\n\n")
                break  # döngüden çıkıp __exit__ e girer
   

def port_selector():
    ports = serial.tools.list_ports.comports()  # listeye dönüştürüp ports un içine attık
    if not ports:
        print("Could not found any serial device!\n")
        return None

    print("Current ports have found!\n")
    for index, port in enumerate(ports):
        print(f"[{index + 1}] - {port.device} - {port.description}")

    try:
        user_choice = int(input("Please enter the number of the port that you want to select: "))
        selected_port = ports[user_choice - 1].device
        print(f"{selected_port} has selected!\n")
        return selected_port
    except (IndexError, ValueError):
        print("The port that you have entered could not found!\n")
        return None

def main():
    try:
        with read_sensor(port_selector()) as reader:
            reader.read_write_sensor()
    except ValueError as error:
        print(f"\n\nSYSTEM CLOSED  --- {error}\n\n")
    except KeyboardInterrupt:
        print("\n\nSystem has manually closed by the user\n\n")

if "__main__" == __name__:
    main()

# with yapısı sadece dosyalara özel bir komut değildir işletim sisteminden ödünç alınan herhangi bir kaynağın (dosya, seri port, veri tabanı, internet bağlantısı) işi bitince kesinlikle iade edilmesini sağlayan bir güvenlik mekanizmasıdır 
# with dosyayı açar (__enter__) ve blok içinde işlemler bitince veya kod çökse bile dosyayı otomatik ve güvenli bir şekilde kapatır
# neden objeyi de with ile çağrıdık? 
# çünkü read_sensor objesi bilgisayar donanımına (USB ye -> arduino dan gelen verileri okumak için) el koyuyor
# bu sayede kullanıcı fişi çekse de ctrl + c ile kapatsa bile program __exit__ a uğrayacak
