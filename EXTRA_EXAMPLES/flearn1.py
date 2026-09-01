import serial
import time

# 1. BAĞLANTIYI KURMA: serial.Serial()
# İlk parametre port adı, ikinci parametre haberleşme hızı (baudrate).
# 'timeout=1' parametresi çok önemlidir: Eğer okuyacak veri yoksa programın
# sonsuza kadar donmasını engeller, 1 saniye bekleyip yoluna devam eder.
ser = serial.Serial('COM3', 9600, timeout=1)

# 2. PORT DURUMUNU KONTROL ETME: is_open
# Portun başka bir program (örneğin Arduino IDE) tarafından meşgul edilip 
# edilmediğini veya başarıyla açılıp açılmadığını kontrol eder. True/False döner.
if ser.is_open:
    print("COM3 portu başarıyla açıldı!")

try:
    # 3. MİKRODENETLEYİCİYE VERİ GÖNDERME: write()
    # Bilgisayardan STM32'ye komut gönderir. write() fonksiyonu SADECE byte kabul eder.
    # 'b' takısı, yazılan sayının veya harfin ham byte olarak iletilmesini sağlar.
    komut_byte = b'\x01'  # Örneğin servoyu hareket ettirecek 1 sayısını byte olarak hazırladık
    ser.write(komut_byte)
    print("STM32'ye komut gönderildi.")

    time.sleep(0.1)  # İşlemcinin veriyi işleyip cevap vermesi için kısa bir süre tanıdık

    while True:
        # 4. BEKLEYEN VERİYİ KONTROL ETME: in_waiting
        # Bilgisayarın veri giriş kapısında (buffer) kaç adet byte'ın okunmayı 
        # beklediğini sayı olarak söyler. Veri yoksa 0 döner.
        if ser.in_waiting > 0:
            
            # 5. BAYTLARI OKUMA: read()
            # Parantez içine yazılan sayı kadar byte okur. 
            # Eğer STM32'den 2 byte'lık bir sensör verisi bekliyorsan buraya read(2) yazarsın.
            # Şu an tamponda ne kadar varsa hepsini okuması için in_waiting değerini verdik.
            okunan_ham_veri = ser.read(ser.in_waiting)
            
            print(f"STM32'den gelen veri: {okunan_ham_veri}")
            # Döngüyü kırıp bitiriyoruz
            break

except KeyboardInterrupt:
    # Klavyeden Ctrl+C'ye basılırsa programın hata vermeden buraya atlamasını sağlar.
    print("Kullanıcı programı durdurdu.")

finally:
    # 6. GÜVENLİ ÇIKIŞ: close()
    # En kritik fonksiyonlardan biridir. Program bitsin veya çöksün, portu mutlaka kapatır.
    # Kapatmazsan port "açık ve meşgul" kalır, kodu ikinci kez çalıştırdığında hata alırsın.
    ser.close()
    print("Port güvenli bir şekilde kapatıldı.")