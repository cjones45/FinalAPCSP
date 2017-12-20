morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", "-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]



word = raw_input(">:")
def index_finder(word, morse, alphabet, index):
    n = 0
    i = index
    for n in range(0, len(alphabet) - 1):
        if word[i] == alphabet[n]:
            return n
        else:
            n += 1


def replace_letter(word, morse, alphabet):
    index = 0
    morse_code = ""
    for n in range(0, len(word)):
        if word[n] in alphabet:
            morse_code += morse[alphabet.index(word[n])] + " "
            index += 1
        elif word[n] not in alphabet:
            morse_code = morse_code + word[n]
    return morse_code


print replace_letter(word, morse, alphabet)
