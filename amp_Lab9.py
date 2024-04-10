#Andrew Price

def encode(passcode):
    new = ''
    for i in range(0, len(passcode)):
        temp = int(passcode[i])
        temp += 3
        if temp > 9:
            temp -= 10
        new += str(temp)
    return new


if __name__ == '__main__':
    while True:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            passcode = input("Please enter your password to encode: ")
            en = encode(passcode)
            print("Your password has been encoded and stored!\n")
        elif choice == 3:
            break
