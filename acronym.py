def acronym(input):
    output = input[0]
    for i in range(len(input)):
        if (input[i] == ' '):
            output += input[i+1]

    return output 

#Purely for testing
if __name__ == "__main__":
    print("Input test string: ")
    teststr = input()
    print(acronym(teststr))