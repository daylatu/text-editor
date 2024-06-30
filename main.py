import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Simple TextEditor")
        self.geometry("900x500")
        ctk.set_appearance_mode("light")


if __name__ == "__main__":
    app = App()
    app.mainloop()
