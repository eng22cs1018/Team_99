from styles import Colors, Fonts

class LoginWindow:
    def __init__(self, root, on_login_success):
        self.root = root
        self.root.configure(bg=Colors.BACKGROUND)
        self.create_login_ui()
        
    def create_login_ui(self):
        main_frame = tk.Frame(self.root, bg=Colors.BACKGROUND)
        main_frame.pack(expand=True, padx=50, pady=50)

        tk.Label(main_frame, text="Welcome Back", font=Fonts.TITLE,
                bg=Colors.BACKGROUND, fg=Colors.DARK).pack(pady=20)

        self.create_input_field(main_frame, "Username", self.username_var)
        self.create_input_field(main_frame, "Password", self.password_var, show="*")

        login_btn = tk.Button(main_frame, text="Sign In", command=self.login,
                             bg=Colors.PRIMARY, fg=Colors.LIGHT, font=Fonts.BUTTON,
                             relief="flat", padx=20, pady=10)
        login_btn.pack(pady=30)
        self.create_button_hover(login_btn, Colors.PRIMARY, "#1565C0")

    def create_input_field(self, parent, label, variable, show=""):
        field_frame = tk.Frame(parent, bg=Colors.BACKGROUND)
        field_frame.pack(fill="x", pady=10)

        entry = tk.Entry(field_frame, textvariable=variable, show=show,
                        font=Fonts.BODY, bd=0, bg=Colors.LIGHT,
                        highlightthickness=2, highlightcolor=Colors.PRIMARY)
        entry.pack(fill="x", ipady=5)

        # Floating label animation
        entry.bind("<FocusIn>", lambda e: self.animate_label(e, label, True))
        entry.bind("<FocusOut>", lambda e: self.animate_label(e, label, False))

    def animate_label(self, event, text, focus):
        entry = event.widget
        if focus or entry.get():
            entry.config(highlightbackground=Colors.PRIMARY)
        else:
            entry.config(highlightbackground="#BDBDBD")