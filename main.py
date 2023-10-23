class MorseCode:

    def code_morse(message):
        alphabet = {
            'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..',
            'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
            'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
            'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--',
            'Я': '.-.-', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', ':': '---...',
            ';': '-.-.-.', '(': '-.--.', ')': '-.--.-', "'": '.----.', '-': '-....-', '/': '-..-.', '_': '..--.-',
            '?': '..--..', '!': '-.-.--', '@': '.--.-.'
        }

        text_morse = ''
        message = message.upper()
        for char in message:
            if char in alphabet:
                text_morse += alphabet[char] + ' '
            else:
                text_morse += ' '
        return text_morse

    def encode_morse(message):
        alphabet = {
            'А': '.-', 'Б': '-...', 'В': '.--', 'Г': '--.', 'Д': '-..', 'Е': '.', 'Ж': '...-', 'З': '--..',
            'И': '..', 'Й': '.---', 'К': '-.-', 'Л': '.-..', 'М': '--', 'Н': '-.', 'О': '---', 'П': '.--.',
            'Р': '.-.', 'С': '...', 'Т': '-', 'У': '..-', 'Ф': '..-.', 'Х': '....', 'Ц': '-.-.', 'Ч': '---.',
            'Ш': '----', 'Щ': '--.-', 'Ъ': '--.--', 'Ы': '-.--', 'Ь': '-..-', 'Э': '..-..', 'Ю': '..--',
            'Я': '.-.-', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
            '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--', ':': '---...',
            ';': '-.-.-.', '(': '-.--.', ')': '-.--.-', "'": '.----.', '-': '-....-', '/': '-..-.', '_': '..--.-',
            '?': '..--..', '!': '-.-.--', '@': '.--.-.'
        }

        words = message.split('  ')
        encode_message = ''
        for char in words:
            letters = char.split(' ')
            for n in letters:
                for key, value in alphabet.items():
                    if value == n:
                        encode_message += key.lower()
                        break
            encode_message += ' '
            morse_text = encode_message.capitalize()
        return morse_text


class CaesarCode:

    def code_caesar(message, shift):

        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        message = message.upper()
        text_caesar = ''
        for i in message:
            place = alphabet.find(i)
            new_place = place + shift
            if i in alphabet:
                text_caesar += alphabet[new_place]
            else:
                text_caesar += i
        return text_caesar.capitalize()

    def encode_caesar(message, shift):
        alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        message = message.upper()
        caesar_text = ''
        for i in message:
            place = alphabet.find(i)
            new_place = place - shift
            if i in alphabet:
                caesar_text += alphabet[new_place]
            else:
                caesar_text += i

        return caesar_text.capitalize()


class HexCode:
    def code_hex(message):
        text_hex = message.encode('utf-8')
        hex_code = text_hex.hex()
        return hex_code

    def encode_hex(message):
        byte_array = bytes.fromhex(message)
        hex_text = byte_array.decode('utf-8')
        return hex_text

