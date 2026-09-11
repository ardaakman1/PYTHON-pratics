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
        self.button_data = ctk.CTkButton(self, text="Read data", command=self.clicked_button, fg_color="blue", state="normal")
        self.button_data.pack(pady=30)

        self.data_screen = ctk.CTkTextbox(self, width=400, height=180, font=("Consolas", 14))
        self.data_screen.pack(pady=20)

    def change_switch(self):
        if self.theme_switch.get() == 1:
            self.theme_switch.configure(text="Dark mode")
            ctk.set_appearance_mode("dark")
        else:
            self.theme_switch.configure(text="light mode")
            ctk.set_appearance_mode("light")

    def clicked_button(self):
        self.state_information.configure(text="Reading the data...")
        self.button_data.configure(text="Reading is completed succesfully", fg_color="green", state="disabled")
        self.data_screen.configure(state="normal")
        self.data_screen.delete("0.0", "end")
        try:
            data_frame = pd.read_csv("value.csv")
            last_data = data_frame.tail(5)
            self.data_screen.insert("0.0", last_data.to_string())
        except FileNotFoundError:
            self.data_screen.insert("0.0", "ERROR --- value.csv could not found\nPlease first start the UART!")

        self.data_screen.configure(state="disabled")
        self.after(2000, self.reset_application)            

    def reset_application(self):
        self.state_information.configure(text="System is waiting")
        self.button_data.configure(text="Read data", fg_color="blue", state="normal")
        self.data_screen.configure(state="normal")
        self.data_screen.delete("0.0", "end")
        self.data_screen.configure(state="disabled")

def main():
    application = data_interface()
    application.mainloop()

if __name__ == "__main__":
    main()