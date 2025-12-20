def is_pangram(sentence):
    EACH_LETTER = []

    for char in sentence:
        char = char.upper()

        if 'A' <= char <= 'Z' and char not in EACH_LETTER:
            EACH_LETTER.append(char)

    if len(EACH_LETTER) == 26:
        return True
    else:
        return False

print("Enter sentence:")
user_input = input()

if is_pangram(user_input):
    print("That sentence is a pangram.")
else:
    print("That sentence is not a pangram.")