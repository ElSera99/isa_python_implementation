"""
Implementation of a small state machine that transcripts the functionality of the regex for: email validation
"""


def read_inputs(path):
    my_file = open(path, 'r', encoding='utf-8')
    emails_list = [element.replace("\n", "") for element in my_file]
    return emails_list


def flow_state_machine(char, state=0):
    upper_case = (
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
        "W",
        "X", "Y", "Z")
    lower_case = (
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
        "w",
        "x", "y", "z")
    digits = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

    if state == 0 and char in upper_case:
        state = 1
    elif state == 1 and char == "_":
        state = 2
    elif state == 2 and char in lower_case:
        state = 2
    elif state == 2 and char in digits:
        state = 3
    elif state == 3 and char in digits:
        state = 4
    elif (state == 2 or state == 4) and char == "@":
        state = 5
    elif state == 5 and char == "e":
        state = 6
    elif state == 6 and char == "v":
        state = 7
    elif state == 7 and char == "i":
        state = 8
    elif state == 8 and char == "l":
        state = 9
    elif state == 9 and char == "c":
        state = 10
    elif state == 10 and char == "o":
        state = 11
    elif state == 11 and char == "r":
        state = 12
    elif state == 12 and char == "p":
        state = 13
    elif state == 13 and char == "o":
        state = 14
    elif state == 14 and char == "r":
        state = 15
    elif state == 15 and char == "a":
        state = 16
    elif state == 16 and char == "t":
        state = 17
    elif state == 17 and char == "i":
        state = 18
    elif state == 18 and char == "o":
        state = 19
    elif state == 19 and char == "n":
        state = 20
    elif state == 20 and char == ".":
        state = 21
    elif state == 21 and char == "c":
        state = 22
    elif state == 22 and char == "o":
        state = 23
    elif state == 23 and char == "m":
        state = 24
    else:
        state = -1

    return state


def compliant(current_state):
    if current_state == 24:
        print("Email compliant")
        return True
    else:
        print("Not compliant")
        return False


def regex_process(my_string):
    print(my_string)
    my_state = 0
    for element in my_string:
        my_state = flow_state_machine(element, my_state)
        if my_state == -1:
            break

    return compliant(my_state)


my_emails = read_inputs("src/emails.txt")
for email in my_emails:
    my_result = regex_process(email)
    print(my_result)
    print("\n")
