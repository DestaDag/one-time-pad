import math



def to_binary(text):
    l,m = [],[]
    for i in text:
        l.append(ord(i))
    for i in l:
        m.append(bin(i)[2:])
    return m


def to_string(binary_txt):
    l = []
    m = ""
    for i in a:
        b = 0
        c = 0
        k = int(math.log(i))+1
        for j in range(k):
            b=((i%10)*(2**j))
            i = i//10
            c=c+b
        l.append(c)
    for x in l:
        m=m+chr(x)
    return m

def main():
    print(to_binary("hello"))


if __name__ == "__main__":
    main()
