import tkinter as tk
from tkinter import ttk
import calendar


class GraphicalCalendar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Graphical Calendar")
        self.geometry("500x500")
        self.calendar = calendar.TextCalendar()

        self.selected_date = None
        self.create_widgets()

    def create_widgets(self):
        self.cal_frame = ttk.Frame(self)
        self.cal_frame.pack(pady=20)

        self.month_label = ttk.Label(self.cal_frame, text="Select Month:")
        self.month_label.grid(row=0, column=0)

        self.month_var = tk.StringVar(self)
        self.month_combobox = ttk.Combobox(
            self.cal_frame,
            textvariable=self.month_var,
            values=[
                "January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"
            ],
        )
        self.month_combobox.grid(row=0, column=1)

        self.year_label = ttk.Label(self.cal_frame, text="Select Year:")
        self.year_label.grid(row=0, column=2)

        self.year_var = tk.StringVar(self)
        self.year_combobox = ttk.Combobox(
            self.cal_frame,
            textvariable=self.year_var,
            values=list(range(1900, 2100))
        )
        self.year_combobox.grid(row=0, column=3)

        self.show_button = ttk.Button(
            self.cal_frame,
            text="Show Calendar",
            command=self.show_calendar
        )
        self.show_button.grid(row=0, column=4)

        self.calendar_text = tk.Text(self, wrap=tk.WORD, height=20, width=30)
        self.calendar_text.pack(pady=10)

    def show_calendar(self):
        month = self.month_combobox.current() + 1
        year = int(self.year_var.get())

        self.selected_date = (year, month)

        self.calendar_text.delete(1.0, tk.END)
        self.calendar_text.insert(tk.END, self.calendar.formatmonth(year, month))


if __name__ == "__main__":
    app = GraphicalCalendar()
    app.mainloop()
