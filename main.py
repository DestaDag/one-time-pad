import random
import string

def random_key(text_len):
    return ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(text_len))


def main():
    print(random_key(len('dagim')))


if __name__ == "__main__":
    main()
