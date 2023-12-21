from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import random


def generate_password():
    password = []
    while len(password) < 14:
        if len(password) < 4:
            password.append(random.choice(ascii_lowercase))
            password.append(random.choice(ascii_uppercase))
            password.append(random.choice(digits))
            password.append(random.choice(punctuation))

        else:
            string_pick = random.randint(1, 4)
            if string_pick == 1:
                password.append(random.choice(ascii_lowercase))
            if string_pick == 2:
                password.append(random.choice(ascii_uppercase))
            if string_pick == 3:
                password.append(random.choice(digits))
            if string_pick == 4:
                password.append(random.choice(punctuation))
    random.shuffle(password)
    return "".join(password)


# print(generate_password())
