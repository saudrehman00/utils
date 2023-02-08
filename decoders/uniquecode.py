#!/usr/bin/python3


codewords = ["101", "1011", "0100", "00101"]

counterExample = ""
index = 0
while len(codewords) != index:
    for codeword in codewords:
        if codewords[index] == codeword:
            continue

        if codeword.startswith(codewords[index]):
            print(codewords)
            print(
                f'"{codewords[index]}" "{codeword}": "{codeword.replace(codewords[index],"",1)}"')
            print()
            if codeword.replace(codewords[index], "", 1) in codewords:
                print("Code is not unique")
                print(counterExample)
                break
            else:
                codewords.append(codeword.replace(codewords[index], "", 1))
                counterExample += codeword.replace(codewords[index], "", 1)
        else:
            print(codewords)
            print(f'{codewords[index]} {codeword}: {""}')
            print()
    index += 1
