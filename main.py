from operator import xor
import random
import string

def random_key(text_len):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(text_len))


def change_to_hex(strng):
    return hex(int(strng, base=16))

def encrypt(text, key_text):
    enc = [(ord(a) ^ ord(b)) for a, b in zip(text, key_text)]
    print(enc)
    for i in range(len(enc)):
        #if enc[i] > 26:
            #enc[i] = enc[i] %26
        enc[i] = chr((enc[i]+ 96))
    return ''.join(enc)

def decrypt(pad, key_text):
    enc = [(ord(a) ^ ord(b)) for a, b in zip(pad, key_text)]
    print(enc)
    for i in range(len(enc)):
        if enc[i] > 26:
            while(enc[i]> 26):
                enc[i] = enc[i] %26
        enc[i] = chr((enc[i]+ 96))
    return ''.join(enc)



def main():
    message = ""
    key = random_key(len(message))
    pad = encrypt(message, key)
    decry = decrypt(pad, key)
    print("message: ",message)
    print("key: ", key)
    print("pad: ", pad)
    print("decrypt: ", decry)



if __name__ == "__main__":
    main()
