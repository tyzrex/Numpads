import tkinter as tk
import itertools

LARGE_FONT_STYLE = ("Arial", 40, "bold")
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
DEFAULT_FONT_STYLE = ("Arial", 20)
OFF_WHITE = "#F8FAFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
letters_by_pad_number = {"3": "def", "9": "wxyz"}

class Numpad:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("345x498")
        self.window.resizable(0, 0)
        self.window.title("Numpad")

        self.current_expression = " "
        self.display_frame = self.create_display_frame()

        self.label = self.create_display_labels()



        self.digits = {
            1: (1, 1), 2: (1, 2), 3: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            7: (3, 1), 8: (3, 2), 9: (3, 3),
            '*': (4, 1), 0: (4, 2), '#': (4, 3)

        }

        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)

        for x in range(1, 4):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def number_to_text(val):
        message = ""
        # change val to string, so we can iterate over digits
        digits = str(val)
        # group consecutive numbers: itertools.groupby("2244") -> ('2', '22'), ('4','44')
        for digit, group in itertools.groupby(digits):
            # get the pad letters, i.e. "def" for "3" pad
            letters = letters_by_pad_number[digit]
            # get how many consecutive times it was pressed
            presses_number = len(list(group))
            # calculate the index of the letter cycling through if we pressed
            # more that 3 times
            letter_index = (presses_number - 1) % len(letters)
            message += letters[letter_index]
        return message


    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.add_to_expression())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

    def create_special_buttons(self):
        self.create_clear_button()
        # self.create_enter_button()

    def create_display_labels(self):
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        # E-position the text at east side
        label.pack(expand=True, fill="both")
        return label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=198, bg = LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
       for digit, grid_value in self.digits.items():
           button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
           button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def clear(self):
        self.current_expression =""
        self.update_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="CLEAR", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, columnspan=4, sticky=tk.NSEW)

    # def create_enter_button(self):
        # button = tk.Button(self.buttons_frame, text="ENTER", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
        # borderwidth=0)
        # button.grid(row=4, column=4, columnspan=4, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_label(self):
        self.label.config(text=self.current_expression[:12])

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    num = Numpad()
    num.run()




