def alpha_position(text):

    output = []

    for letter in text.lower():
        if letter.isalpha():
            position = ord(letter) - ord("a") + 1
            output.append(str(position))
    return " ".join(output)

print(alpha_position("The sunset sets at twelve o' clock."))