import customtkinter as ctk

class data_interface(ctk.CTk):
# ctk.CTk sınıfından miras alıyoruz (Inheritance); böylece pencerenin 
# tüm temel özelliklerini (boyut, kapatma tuşu vb.) sıfırdan yazmadan devralıyoruz.
    def __init__(self):
        super().__init__()  # inheritence CTk class ının tüm özelliklerini alıyoruz
        self.title("Embedded systems panel!")
        self.geometry("500x300")  # genişlik x yükseklik formunda tırnak içine yazılır

        # CTkLabel: Arayüze kullanıcıya bilgi vermek amaçlı tıklanamayan, düz bir metin (etiket) ekleyen araçtır.
        # 1. parametre 'self' -> Bu yazının dışarıda değil, direkt "bu pencerenin içinde" olacağını belirtir.
        # 2. parametre 'text' -> Ekranda göstereceğimiz cümle.
        # 3. parametre 'font' -> Yazı tipini (Arial) ve büyüklüğünü (20 punto) belirler.
        self.state_information = ctk.CTkLabel(self, text="System is waiting...", font=("Arial", 20))
        # pack(): Hafızada oluşturduğumuz yukarıdaki yazıyı, pencerenin içine görünür şekilde yerleştiren (paketleyen) komuttur. Ekrana hizalar.
        # pady=30 (Padding-Y): Y ekseninde (dikeyde) yazının üstünden ve altından 30 piksel boşluk (yastıklama) bırakır. Yazının pencerenin tepesine yapışmasını engeller.
        self.state_information.pack(pady=30)

        self.data_button = ctk.CTkButton(self, text="Read data", command=self.clicked_button)
        self.data_button.pack(pady=10)

    def clicked_button(self):  # butonun tetikleyeceği fonksiyon
        self.state_information.configure(text="CSV file is reading!")  # configure() komutu, daha önce oluşturduğumuz objenin özelliklerini günceller
        self.data_button.configure(text="Reading is succefully completed", fg_color="green")
        # Foreground Color (fg_color) butonun kendi rengini belirler yani tıklandıktan sonra yeşil olur
        self.after(2000, self.reset_application)  # 2 saniye bekle ve reset application çalıştır

    def reset_application(self):
        self.state_information.configure(text="System is waiting...")
        self.data_button.configure(text="Read data", command=self.clicked_button)  # burda clicked_button() yazmadım bu sayede fonksiyonun adresni button a yollamış oldum zaten command aslen adres bekler 

def main():
    application = data_interface()
    application.mainloop()  # daha gelişmiş while True:

if __name__ == "__main__":
    main()

# mainloop() Farkı: mainloop() aslında kütüphaneyi yazan mühendislerin oluşturduğu çok gelişmiş bir sonsuz döngüdür. İçinde işletim sistemiyle sürekli konuşan bir yapı vardır.
# Her milisaniyede işletim sistemine "Kullanıcı fareyi oynattı mı? Ekranda yeniden çizmem gereken bir yazı var mı?" diye sorar. Yani senin yerine arayüzü hayatta tutan döngüyü zaten kendi içinde barındırır.
