from tkinter import *
from functools import partial


class Converter():
    """
    Currency Conversion Tool (NZD to AUD, USD and GBP)
    """

    def __init__(self):
        # Current exchange rates from google search
        self.rates = {
            "NZD to AUD": 0.81, "AUD to NZD": 1.23,
            "NZD to USD": 0.57, "USD to NZD": 1.75,
            "NZD to GBP": 0.43, "GBP to NZD": 2.32
        }

        self.all_calculations_list = []

        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        self.heading = Label(self.currency_frame,
                             text="Currency Converter",
                             font=("Arial", "16", "bold"))
        self.heading.grid(row=0)

        instructions = ("Enter the amount you wish to convert, "
                        "select the currency pair, and press Convert.")
        self.instructions = Label(self.currency_frame,
                                  text=instructions,
                                  wraplength=250, width=40,
                                  justify="left")
        self.instructions.grid(row=1)

        # dropdown menu
        self.currency_options = [
            "NZD to AUD", "AUD to NZD",
            "NZD to USD", "USD to NZD",
            "NZD to GBP", "GBP to NZD"
        ]
        self.selected_conversion = StringVar()
        self.selected_conversion.set(self.currency_options[0])

        self.conversion_menu = OptionMenu(self.currency_frame,
                                          self.selected_conversion,
                                          *self.currency_options)
        self.conversion_menu.config(width=15, font=("Arial", "11"))
        self.conversion_menu.grid(row=2, padx=10, pady=10)

        self.amount_entry = Entry(self.currency_frame, font=("Arial", "14"))
        self.amount_entry.grid(row=3, padx=10, pady=10)

        error = "Enter an amount to convert"
        self.output_label = Label(self.currency_frame, text=error,
                                  fg="#004C99", font=("Arial", "13", "bold"))
        self.output_label.grid(row=4)

        # Buttons
        self.button_frame = Frame(self.currency_frame)
        self.button_frame.grid(row=5)

        button_details = [
            ["Convert", "#009900", self.check_amount, 0, 0],
            ["History / Export", "#004C99", self.to_history, 1, 0],
        ]

        self.button_ref_list = []
        for item in button_details:
            btn = Button(self.button_frame, text=item[0], bg=item[1],
                         fg="#FFFFFF", font=("Arial", "12", "bold"),
                         width=12, command=item[2])
            btn.grid(row=item[3], column=item[4], padx=5, pady=5)
            self.button_ref_list.append(btn)

        self.to_history_button = self.button_ref_list[1]
        self.to_history_button.config(state=DISABLED)

    def check_amount(self):
        """Validates input and triggers conversion"""
        amount = self.amount_entry.get()
        self.amount_entry.config(bg="#FFFFFF")

        try:
            amount = float(amount)
            if amount > 0:
                self.convert(amount)
            else:
                self.show_error("Enter a number greater than 0")
        except ValueError:
            self.show_error("Enter a valid number")

    def convert(self, amount):
        """Performs calculation based on selected dropdown option"""
        conversion_type = self.selected_conversion.get()
        rate = self.rates[conversion_type]

        # Split string to get currency names, for example: NZD to USD
        currencies = conversion_type.split(" to ")
        from_cur = currencies[0]
        to_cur = currencies[1]

        result = amount * rate
        # Formatting to 2 decimal places for money
        answer_statement = f"{amount:.2f} {from_cur} is {result:.2f} {to_cur}"

        self.output_label.config(text=answer_statement, fg="#004C99")
        self.all_calculations_list.append(answer_statement)
        self.to_history_button.config(state=NORMAL)

    def show_error(self, message):
        self.output_label.config(text=message, fg="#9C0000")
        self.amount_entry.config(bg="#F4CCCC")

    def to_history(self):
        HistoryExport(self, self.all_calculations_list)


class HistoryExport:
    def __init__(self, partner, calculations):
        self.history_box = Toplevel()
        partner.to_history_button.config(state=DISABLED)
        self.history_box.protocol('WM_DELETE_WINDOW', partial(self.close_history, partner))

        Label(self.history_box, text="Calculation History", font=("Arial", "14", "bold")).pack(pady=10)

        # Simplified history display for this example
        history_text = "\n".join(calculations[-5:])  # Show last 5
        Label(self.history_box, text=history_text).pack(padx=20, pady=10)

        Button(self.history_box, text="Close", command=partial(self.close_history, partner)).pack(pady=10)

    def close_history(self, partner):
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()