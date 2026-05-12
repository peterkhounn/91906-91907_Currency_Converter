from tkinter import *
from functools import partial


class Converter():
    """
    Currency Conversion Tool (NZD to AUD, USD and GBP)
    """

    def __init__(self):
        self.currency_frame = Frame(padx=10, pady=10)
        self.currency_frame.grid()

        self.to_help_button = Button(self.currency_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg="#FFFFFF",
                                     font=("Arial", "12", "bold"),
                                     width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=0, column=0, padx=5, pady=5)

    def to_help(self):
        """Triggers the help window"""
        DisplayHelp(self)


class DisplayHelp:
    def __init__(self, partner):
        self.help_box = Toplevel()
        # Disable the main button so multiple help windows cannot be opened
        partner.to_help_button.config(state=DISABLED)

        # Handle the window close button (X)
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        help_text = ("Choose your currency pair from the dropdown, "
                     "enter the amount, and click Convert. \n\n"
                     "You can view and export your history using the "
                     "History/Export button.")

        Label(self.help_box, text="Help / Info", font=("Arial", "14", "bold")).pack(pady=10)
        Label(self.help_box, text=help_text, wraplength=250).pack(padx=20, pady=10)

        # Dismiss button
        Button(self.help_box, text="Dismiss",
               command=partial(self.close_help, partner)).pack(pady=10)

    def close_help(self, partner):
        """Re-enables the help button and closes the help window"""
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()


if __name__ == "__main__":
    root = Tk()
    root.title("Currency Converter")
    Converter()
    root.mainloop()