import os
from .styles import Colors, Fonts, StyleHelper
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model
import random

# Sample patient records for demonstration
PATIENTS = [
    {'Name': 'John Doe',  'Age': '58', 'Gender': 'Male',   'ID': 'PT001'},
    {'Name': 'Jane Smith','Age': '66', 'Gender': 'Female', 'ID': 'PT002'},
    {'Name': 'Alan Lee',  'Age': '72', 'Gender': 'Male',   'ID': 'PT003'},
]

# Determine the model path relative to the project root
SRC_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SRC_DIR)
MODEL_PATH = os.path.join(PROJECT_ROOT, 'model', 'rwma_resnet50_model.h5')
CLASS_NAMES = ['Normal', 'Abnormal']

# Load the pre-trained model
model = load_model(MODEL_PATH, compile=False)

class EchoFrame(tk.Frame):
    PREVIEW_SIZE = (180, 180)  # Increased Width, height for preview

    def __init__(self, parent, main_app):
        super().__init__(parent, bg=Colors.BACKGROUND)
        self.main_app = main_app
        self.selected_file = None
        self.original_image = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(
            self, text="Echo Image Analysis", font=Fonts.TITLE,
            bg=Colors.BACKGROUND, fg=Colors.PRIMARY
        ).pack(pady=(20, 10))

        upload_frame = StyleHelper.create_card(self, "Upload Echo Image", "")
        upload_frame.pack(pady=20, padx=20, fill="x")

        self.upload_btn = tk.Button(
            upload_frame, text="Choose File", command=self.upload_image,
            bg=Colors.SECONDARY, fg=Colors.LIGHT, font=Fonts.BUTTON,
            relief="raised", bd=2
        )
        self.upload_btn.pack(side='left', padx=10, pady=20)

        self.predict_btn = tk.Button(
            upload_frame, text="Predict", command=self.predict_image,
            bg=Colors.PRIMARY, fg=Colors.LIGHT, font=Fonts.BUTTON,
            relief="raised", bd=2, state='disabled'
        )
        self.predict_btn.pack(side='right', padx=10, pady=20)

        content_frame = tk.Frame(self, bg=Colors.BACKGROUND)
        content_frame.pack(fill="both", expand=True, padx=20, pady=20)

        img_card = StyleHelper.create_card(content_frame, "Image Preview", "")
        img_card.pack(side="left", fill="both", expand=True, padx=10, pady=10)
        # Use Canvas to ensure precise pixel dimensions and fill area
        self.preview_canvas = tk.Canvas(
            img_card,
            width=self.PREVIEW_SIZE[0],
            height=self.PREVIEW_SIZE[1],
            bg=Colors.LIGHT,
            highlightthickness=0  # remove border
        )
        self.preview_canvas.pack(fill="both", expand=True) #, padx=150, pady=0
        self.preview_canvas.place(relx=0.5, rely=0.5, anchor='center')

        self.details_card = StyleHelper.create_card(
            content_frame, "Patient Information", ""
        )
        self.details_card.pack(side="right", fill="both", expand=True, padx=10, pady=10)
        self.create_detail_labels({
            "Name": "--", "Age": "--", "Gender": "--",
            "ID": "--", "Result": "--"
        })

        slide_frame = tk.Frame(self, bg=Colors.BACKGROUND)
        slide_frame.pack(pady=10, padx=20, fill="x")
        tk.Label(
            slide_frame, text="Adjust Analysis Sensitivity:", font=Fonts.BODY,
            bg=Colors.BACKGROUND, fg=Colors.DARK
        ).pack(side="left", padx=10)

        self.sensitivity_var = tk.DoubleVar(value=50)
        scale = tk.Scale(
            slide_frame, from_=0, to=100, orient="horizontal",
            variable=self.sensitivity_var, bg=Colors.LIGHT, fg=Colors.DARK,
            troughcolor=Colors.SECONDARY, highlightbackground=Colors.BACKGROUND
        )
        scale.pack(side="left", fill="x", expand=True, padx=10)

        tk.Label(
            self, text="Powered by Heart Analysis AI",
            font=Fonts.FOOTER, bg=Colors.BACKGROUND, fg=Colors.SECONDARY
        ).pack(pady=(10, 20))

    def create_detail_labels(self, details):
        for widget in self.details_card.winfo_children():
            widget.destroy()
        for key, value in details.items():
            row = tk.Frame(self.details_card, bg=Colors.LIGHT, relief="ridge", bd=1)
            row.pack(fill="x", pady=5, padx=5)
            tk.Label(
                row, text=f"{key}:", font=Fonts.BODY, bg=Colors.LIGHT,
                width=15, anchor="w", fg=Colors.DARK
            ).pack(side="left")
            tk.Label(
                row, text=value, font=Fonts.BODY, bg=Colors.LIGHT,
                fg=Colors.PRIMARY
            ).pack(side="left")

    def upload_image(self):
        file_path = filedialog.askopenfilename(
            title="Select an Echo Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")]
        )
        if not file_path:
            return
        self.selected_file = file_path
        # Load original image
        self.original_image = Image.open(file_path)
        # Resize for larger consistent preview size
        preview_img = self.original_image.resize(self.PREVIEW_SIZE, Image.LANCZOS)
        photo = ImageTk.PhotoImage(preview_img)
        # Display on canvas
        self.preview_canvas.delete("all")
        # Center image in canvas
        canvas_w, canvas_h = self.PREVIEW_SIZE
        self.preview_canvas.create_image(
            canvas_w/2,
            canvas_h/2,
            anchor='center',
            image=photo
        )
        self.preview_canvas.image = photo
        self.predict_btn.config(state='normal')
        self.create_detail_labels({
            "Name": "--", "Age": "--", "Gender": "--",
            "ID": "--", "Result": "--"
        })
        self.main_app.show_prediction()

    def predict_image(self):
        if not self.selected_file:
            messagebox.showwarning("No Image", "Please select an image first.")
            return
        try:
            img = self.original_image.convert('RGB').resize((224, 224), Image.LANCZOS)
            arr = np.expand_dims(np.array(img) / 255.0, axis=0)
            preds = model.predict(arr)
            idx = int(np.argmax(preds, axis=1)[0])
            result = CLASS_NAMES[idx]
            confidence = float(np.max(preds))
        except Exception as e:
            messagebox.showerror("Prediction Error", str(e))
            result, confidence = "Error", 0.0
        patient = random.choice(PATIENTS)
        details = {
            'Name': patient['Name'], 'Age': patient['Age'],
            'Gender': patient['Gender'], 'ID': patient['ID'],
            'Result': f"{result} ({confidence:.2f})"
        }
        self.create_detail_labels(details)
        self.sensitivity_var.set(50)