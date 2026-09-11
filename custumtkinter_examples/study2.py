import customtkinter as ctk

class data_interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Embedded values application")
        self.geometry("500x300")
        self.state_information = ctk.CTkLabel(self, text="System is waiting...", font=("Arial", 20))
        self.state_information.pack(pady=30)
        self.data_button = ctk.CTkButton(self, text="Read data", command=self.clicked_button)
        self.data_button.pack(pady=10)

    def clicked_button(self):
        self.state_information.configure(text="CSV file is reading")
        self.data_button.configure(text="Reading is succesfully completed!", fg_color="green", state="disabled")
        self.after(2000, self.reset_application)

    def reset_application(self):
        self.state_information.configure(text="System is waiting...")
        self.data_button.configure(text="Read data", fg_color="blue", state="normal")  # state ile butona tıklayonca 2 saniye boyunca tekrar rıklanılamamasını ekledik

def main():
    application = data_interface()
    application.mainloop()

if __name__ == "__main__":
    main()