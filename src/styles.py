import tkinter as tk

# styles.py
class Colors:
    PRIMARY = "#1976D2"
    SECONDARY = "#607D8B"
    SUCCESS = "#4CAF50"
    INFO = "#2196F3"
    WARNING = "#FFC107"
    DANGER = "#F44336"
    LIGHT = "#FFFFFF"
    DARK = "#212121"
    BACKGROUND = "#F5F5F5"

class Fonts:
    TITLE = ("Roboto", 18, "bold")
    SUBTITLE = ("Roboto", 14)
    BODY = ("Roboto", 12)
    BUTTON = ("Roboto", 12, "bold")
    FOOTER = ("Roboto", 10, "italic")

class StyleHelper:
    @staticmethod
    def create_card(parent, title, content, bg_color=Colors.LIGHT):
        card_frame = tk.Frame(parent, bg=bg_color, bd=1, relief="solid",
                             highlightbackground="#BDBDBD", highlightthickness=1)
        card_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        tk.Label(card_frame, text=title, font=Fonts.SUBTITLE, 
                 bg=bg_color, fg=Colors.DARK).pack(pady=10, anchor="w")
        tk.Label(card_frame, text=content, font=("Roboto", 24, "bold"), 
                 bg=bg_color, fg=Colors.PRIMARY).pack(pady=10)
        
        return card_frame