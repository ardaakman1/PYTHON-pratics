import customtkinter as ctk

class data_interface(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Embedded Values")
        self.geometry("500x400")
        self.theme_switch = ctk.CTkSwitch(self, text="Dark mode", command=self.change_theme)
        self.theme_switch.pack(pady=10)
        self.theme_switch.select()  # en başta tema seçili gelsin
        self.state_information = ctk.CTkLabel(self, text="System is waiting", font=("Arial", 20))
        self.state_information.pack(pady=30)
        self.data_button = ctk.CTkButton(self, text="Read data", fg_color="blue", command=self.clicked_button)
        self.data_button.pack(pady=30)

    def change_theme(self):
        if self.theme_switch.get() == 1:  # get şalterin açık / kapalı olduğunu görür
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def clicked_button(self):
        self.state_information.configure(text="CSV file is reading")
        self.data_button.configure(text="Reading is completed succesfully", fg_color="green", state="disabled")
        self.after(2000, self.reset_application)

    def reset_application(self):
        self.state_information.configure(text="System is waiting")
        self.data_button.configure(text="Read data", fg_color="blue", state="normal")

def main():
    application = data_interface()
    application.mainloop()

if __name__ == "__main__":
    main()