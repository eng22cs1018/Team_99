from .styles import Colors, Fonts, StyleHelper
import tkinter as tk
import datetime

# Placeholder functions for metrics
def get_total_patients():
    return "120"

def get_today_appointments():
    return "15"

def get_pending_reports():
    return "8"

def get_new_messages():
    return "5"

class DashboardFrame(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg=Colors.BACKGROUND)
        self.create_widgets()

    def create_widgets(self):
        # Header Section
        header_frame = tk.Frame(self, bg=Colors.PRIMARY)
        header_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(header_frame, text="Doctor Dashboard", font=Fonts.TITLE,
                fg=Colors.LIGHT, bg=Colors.PRIMARY).pack(side="left", padx=20, pady=10)

        self.time_label = tk.Label(header_frame, font=Fonts.SUBTITLE,
                                  fg=Colors.LIGHT, bg=Colors.PRIMARY)
        self.time_label.pack(side="right", padx=20)
        self.update_time()

        # Metrics Cards
        metrics_frame = tk.Frame(self, bg=Colors.BACKGROUND)
        metrics_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.metric_cards = [
            StyleHelper.create_card(metrics_frame, "Total Patients", get_total_patients()),
            StyleHelper.create_card(metrics_frame, "Today's Appointments", get_today_appointments()),
            StyleHelper.create_card(metrics_frame, "Pending Reports", get_pending_reports()),
            StyleHelper.create_card(metrics_frame, "New Messages", get_new_messages())
        ]
        
        # Arrange cards using pack
        for card in self.metric_cards:
            card.pack(fill="x", pady=10)

    def update_time(self):
        now = datetime.datetime.now().strftime("%A, %d %B %Y | %I:%M %p")
        self.time_label.config(text=now)
        self.after(1000, self.update_time)