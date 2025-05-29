from .styles import Colors, Fonts
from .dashboard import DashboardFrame
from .prediction_page import EchoFrame
import tkinter as tk

class MainApp:
    def __init__(self, root):
        self.root = root

        # Define the main content area
        self.main_frame = tk.Frame(self.root, bg=Colors.LIGHT)
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.build_main_ui()

        # Initialize frames
        self.dashboard_frame = DashboardFrame(self.main_frame)
        self.echo_frame = EchoFrame(self.main_frame, self)

        # Show the dashboard by default
        self.show_dashboard()
    
    def build_main_ui(self):
        sidebar = tk.Frame(self.root, bg=Colors.PRIMARY, width=240)
        sidebar.pack(side="left", fill="y")

        tk.Label(sidebar, text="Echo Analyzer", font=Fonts.TITLE,
                 bg=Colors.PRIMARY, fg=Colors.LIGHT).pack(pady=30)

        buttons = [
            ("Dashboard", self.show_dashboard),
            ("Echo Upload", self.show_prediction),
            ("Reports", lambda: None),
            ("Messages", lambda: None)
        ]

        for text, cmd in buttons:
            btn = tk.Button(sidebar, text=text, command=cmd,
                            font=Fonts.BUTTON, bg=Colors.PRIMARY, fg=Colors.LIGHT,
                            relief="flat", anchor="w", padx=20)
            btn.pack(fill="x", pady=8)
            self.create_button_hover(btn, "#1565C0")

    def create_button_hover(self, button, hover_color):
        button.bind("<Enter>", lambda e: button.config(bg=hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=Colors.PRIMARY))

    def show_dashboard(self):
        # Hide other frames instead of destroying them
        self.echo_frame.pack_forget()

        # Display the dashboard frame
        self.dashboard_frame.pack(fill="both", expand=True)

    def show_prediction(self):
        # Hide other frames instead of destroying them
        self.dashboard_frame.pack_forget()

        # Display the echo frame
        self.echo_frame.pack(fill="both", expand=True)