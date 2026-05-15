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

        self.output_label = Label(self.currency_frame,
                                  fg="#004C99", font=("Arial", "13", "bold"))
        self.output_label.grid(row=4)


if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()