import customtkinter as ctk
import pandas as pd

class data_interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Embedded Values")
        self.geometry("500x500")
        self.theme_switch = ctk.CTkSwitch(self, text="Dark mode", command=self.change_switch)
        self.theme_switch.pack(pady=10)
        self.theme_switch.select()
        self.state_information = ctk.CTkLabel(self, text="System is waiting", font=("Arial", 20))
        self.state_information.pack(pady=30)
        self.button_data = ctk.CTkButton(self, text="Read Data", fg_color="blue", command=self.clicked_button, state="normal")
        self.button_data.pack(pady=30)

        self.data_screen = ctk.CTkTextbox(self, width=400, height=180, font=("Consolas", 14))
        self.data_screen.pack(pady=20)

    def change_switch(self):
        if self.theme_switch.get() == 1:
            self.theme_switch.configure(text="Light mode")
            ctk.set_appearance_mode("dark")
        else:
            self.theme_switch.configure(text="Dark mode")
            ctk.set_appearance_mode("light")

    def clicked_button(self):
        self.state_information.configure(text="Reading the data...")
        self.button_data.configure(text="Reading is completed succesfully", fg_color="green", state="disabled")
        self.data_screen.configure(state="normal")
        self.data_screen.delete("0.0", "end")
        try:
            data_frame= pd.read_csv("values.csv")  # dosyayı oku ve data frame e çevir
            last_data = data_frame.tail(5)  # tüm dosyayı değil sadece en alttaki 5 satırı al 
            self.data_screen.insert("0.0", last_data.to_string()) # veriyi metne çevir ve frame e bas

        except FileNotFoundError:
            self.data_screen.insert("0.0", "ERROR --- value.csv could not found\nPlease first start the UART!")

        self.data_screen.configure(state="disabled")
        self.after(2000, self.reset_application)
        


    def reset_application(self):
        self.state_information.configure(text="System is waiting")
        self.button_data.configure(text="Read Data", fg_color="blue", state="normal")
        self.data_screen.configure(state="normal")
        self.data_screen.delete("0.0", "end")
        self.data_screen.configure(state="disabled")

def main():
    application = data_interface()
    application.mainloop()

if __name__ == "__main__":
    main()


# delete(): Kutunun içindeki yazıları silmeye yarayan fonksiyon.

# "0.0" (Nereden başlanacak?): Tkinter ve CustomTkinter dünyasında metin kutuları koordinat sistemiyle çalışır. Buradaki format Satır.Sütun şeklindedir. "0.0" yazdığımızda sisteme şunu söyleriz: "0.inci satırın, 0.inci karakterinden (yani metin kutusunun en sol üst köşesinden) işlem yapmaya başla."

# "end" (Nereye kadar silinecek?): Bu da bitiş noktasıdır. Metin kutusunun en son karakterine kadar her şeyi sil anlamına gelir.