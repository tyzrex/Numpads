import itertools

letters_by_pad_number = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mnop", "7": "qrs", "8": "tuv", "9": "wxyz"}
num = int(input("Enter number: "))

def number_to_text(val):
    message = ""
    digits = str(val)
    for digit, group in itertools.groupby(digits):
        letters = letters_by_pad_number[digit]
        presses_number = len(list(group))
        letter_index = (presses_number - 1) % len(letters)
        message += letters[letter_index]
    return message

print(number_to_text(num))