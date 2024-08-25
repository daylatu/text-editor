import customtkinter as ctk
from customtkinter import filedialog

ctk.set_appearance_mode("light")

# Main gui:
app = ctk.CTk()
app.geometry("900x600")
app.title("Simple TextEditor")
app.resizable(width=False, height=False)
mainfont = ctk.CTkFont(family="Consolas", size=15)

# TextBox:
textbox = ctk.CTkTextbox(app, font=mainfont, width=890, height=575, corner_radius=8)
textbox.pack(side=ctk.BOTTOM)

current_filepath = None


# Function :
def open_file():
    global current_filepath
    filepath = filedialog.askopenfilename(
        filetypes=[("Text file", "*.txt"), ("All files", "*.*")]
    )
    if not filepath:
        return
    textbox.delete("0.0", "end")
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        textbox.insert("0.0", text)
        app.title(f"Simple TextEditor - {filepath}")
    current_filepath = filepath


def save_fileas():
    global current_filepath
    filepath = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text file", "*.txt"), ("All files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = textbox.get("0.0", "end")
        output_file.write(text)
        app.title(f"Simple TextEditor - {filepath}")
    current_filepath = filepath


def save_file():
    global current_filepath
    if not current_filepath:
        save_fileas()
    else:
        with open(current_filepath, mode="w", encoding="utf-8") as output_file:
            text = textbox.get("0.0", "end")
            output_file.write(text)
            app.title(f"Simple TextEditor - {current_filepath}")


# Button
fileopen = ctk.CTkButton(
    app,
    text="Open",
    font=mainfont,
    text_color="black",
    fg_color="white",
    width=40,
    hover_color="#C0ECF3",
    command=open_file,
)
filesaveas = ctk.CTkButton(
    app,
    text="Save as",
    font=mainfont,
    fg_color="white",
    text_color="black",
    width=40,
    hover_color="#C0ECF3",
    command=save_fileas,
)
filesave = ctk.CTkButton(
    app,
    text="Save",
    font=mainfont,
    fg_color="white",
    text_color="black",
    width=40,
    hover_color="#C0ECF3",
    command=save_file,
)

fileopen.pack(anchor="nw", side="left", padx=3)
filesave.pack(anchor="nw", side="left", padx=3)
filesaveas.pack(anchor="nw", side="left", padx=3)

app.mainloop()
