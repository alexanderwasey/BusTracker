def acronym(input):

    #Makes the last word an acronym until until the word is short enough 
    #Split the output into 2 halves 
    output = input 
    initials = ""

    while len(output + initials)> 14:
        #Remove the last word in the output string 
        i = len(output) - 2
        while True:
            if i < 0:
                break
            elif output[i] == ' ':
                initials = output[i+1] + initials
                output = output[:-1]
                break
            else: 
                output = output[:-1]
                i = i - 1

    return output + initials 

#Purely for testing
if __name__ == "__main__":
    print("Input test string: ")
    teststr = input()
    print(acronym(teststr))
