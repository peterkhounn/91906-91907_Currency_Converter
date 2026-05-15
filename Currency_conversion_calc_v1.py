from tkinter import *


class Converter():
    """
    Currency Conversion Tool (NZD to AUD, USD and GBP)
    """

    def __init__(self):

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
            ["Convert", "#009900", 0, 0],
        ]

        self.button_ref_list = []
        for item in button_details:
            btn = Button(self.button_frame, text=item[0], bg=item[1],
                         fg="#FFFFFF", font=("Arial", "12", "bold"),
                         width=12, command=item[2])
            btn.grid(row=item[3], padx=5, pady=5)
            self.button_ref_list.append(btn)


if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()