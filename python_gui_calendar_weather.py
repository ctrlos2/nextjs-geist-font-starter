import tkinter as tk
from tkinter import ttk
import calendar
from datetime import datetime

class NeonCalendarWeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nowoczesny Kalendarz i Pogoda")
        self.configure(bg="#121212")
        self.geometry("700x400")
        self.resizable(False, False)

        # Styles
        self.style = ttk.Style(self)
        self.style.theme_use('clam')
        self.style.configure("TButton",
                             background="#1E90FF",
                             foreground="white",
                             font=("Segoe UI", 10, "bold"),
                             borderwidth=0,
                             focusthickness=3,
                             focuscolor='none')
        self.style.map("TButton",
                       background=[('active', '#63B8FF')])

        # Neon blue label style
        self.neon_blue = "#00BFFF"
        self.neon_bg = "#121212"
        self.text_font = ("Segoe UI", 14, "bold")
        self.small_font = ("Segoe UI", 10)
        self.title_font = ("Segoe UI", 18, "bold")

        # Layout frames
        self.calendar_frame = tk.Frame(self, bg=self.neon_bg)
        self.weather_frame = tk.Frame(self, bg=self.neon_bg)

        self.calendar_frame.place(relx=0.05, rely=0.1, relwidth=0.45, relheight=0.8)
        self.weather_frame.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.8)

        # Title
        title_label = tk.Label(self, text="Nowoczesny Kalendarz i Pogoda",
                               font=self.title_font, fg=self.neon_blue, bg=self.neon_bg)
        title_label.place(relx=0.5, rely=0.02, anchor="n")

        # Calendar controls
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month
        self.selected_day = datetime.now().day

        self.create_calendar_controls()
        self.create_calendar()
        self.create_weather_panel()

    def create_calendar_controls(self):
        control_frame = tk.Frame(self.calendar_frame, bg=self.neon_bg)
        control_frame.pack(pady=10)

        prev_btn = tk.Button(control_frame, text="<", command=self.prev_month,
                             bg=self.neon_bg, fg=self.neon_blue, font=self.text_font,
                             borderwidth=0, activebackground="#0F4C81", activeforeground=self.neon_blue)
        prev_btn.pack(side="left", padx=10)

        self.month_year_label = tk.Label(control_frame, text="", font=self.text_font,
                                         fg=self.neon_blue, bg=self.neon_bg)
        self.month_year_label.pack(side="left", padx=10)

        next_btn = tk.Button(control_frame, text=">", command=self.next_month,
                             bg=self.neon_bg, fg=self.neon_blue, font=self.text_font,
                             borderwidth=0, activebackground="#0F4C81", activeforeground=self.neon_blue)
        next_btn.pack(side="left", padx=10)

    def create_calendar(self):
        # Clear previous calendar if any
        if hasattr(self, 'calendar_days_frame'):
            self.calendar_days_frame.destroy()

        self.calendar_days_frame = tk.Frame(self.calendar_frame, bg=self.neon_bg)
        self.calendar_days_frame.pack()

        # Polish weekdays short names
        weekdays = ["Pon", "Wt", "Śr", "Czw", "Pt", "Sob", "Ndz"]
        for i, day in enumerate(weekdays):
            lbl = tk.Label(self.calendar_days_frame, text=day, font=self.small_font,
                           fg=self.neon_blue, bg=self.neon_bg, width=4)
            lbl.grid(row=0, column=i, padx=2, pady=2)

        cal = calendar.Calendar(firstweekday=0)  # Monday as first day
        month_days = cal.itermonthdays(self.current_year, self.current_month)

        row = 1
        col = 0
        for day in month_days:
            if day == 0:
                # days outside the month
                lbl = tk.Label(self.calendar_days_frame, text=" ", bg=self.neon_bg, width=4)
                lbl.grid(row=row, column=col, padx=2, pady=2)
            else:
                if (day == self.selected_day and
                    self.current_year == datetime.now().year and
                    self.current_month == datetime.now().month):
                    bg_color = "#1E90FF"
                    fg_color = "white"
                else:
                    bg_color = self.neon_bg
                    fg_color = self.neon_blue

                lbl = tk.Label(self.calendar_days_frame, text=str(day), font=self.small_font,
                               fg=fg_color, bg=bg_color, width=4, relief="flat", borderwidth=0)
                lbl.grid(row=row, column=col, padx=2, pady=2)

            col += 1
            if col > 6:
                col = 0
                row += 1

        # Update month year label
        month_name = calendar.month_name[self.current_month]
        # Polish month names (abbreviated)
        polish_months = {
            "January": "Styczeń",
            "February": "Luty",
            "March": "Marzec",
            "April": "Kwiecień",
            "May": "Maj",
            "June": "Czerwiec",
            "July": "Lipiec",
            "August": "Sierpień",
            "September": "Wrzesień",
            "October": "Październik",
            "November": "Listopad",
            "December": "Grudzień"
        }
        month_name_pl = polish_months.get(month_name, month_name)
        self.month_year_label.config(text=f"{month_name_pl} {self.current_year}")

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.create_calendar()

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.create_calendar()

    def create_weather_panel(self):
        # Title
        weather_title = tk.Label(self.weather_frame, text="Błąd pogodowy",
                                 font=self.title_font, fg=self.neon_blue, bg=self.neon_bg)
        weather_title.pack(pady=(10, 5))

        # Error symbol
        error_symbol = tk.Label(self.weather_frame, text="-",
                                font=("Segoe UI", 40, "bold"), fg=self.neon_blue, bg=self.neon_bg)
        error_symbol.pack(pady=5)

        # Error message
        error_message = tk.Label(self.weather_frame,
                                 text="Nie Udało Się Pobrać Pogody.",
                                 font=self.small_font, fg=self.neon_blue, bg=self.neon_bg, wraplength=200, justify="center")
        error_message.pack(pady=5)

        # Refresh button
        refresh_btn = ttk.Button(self.weather_frame, text="Odśwież pogodę", command=self.refresh_weather)
        refresh_btn.pack(pady=15)

    def refresh_weather(self):
        # Simulate refresh - just update the error message with a flash effect
        # For now, just print to console
        print("Odświeżanie pogody... (symulacja)")

if __name__ == "__main__":
    app = NeonCalendarWeatherApp()
    app.mainloop()
