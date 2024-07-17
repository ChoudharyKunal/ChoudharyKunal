vowals = ["a","e","i","o","u"]

sample_string = input("add String")

def vowInString(sample_string):
    for i in range(len(sample_string)):
        if sample_string[i] in vowals:
            newString = newString+sample_string[i]

    print(newString)



print(print(vowInString(sample_string)))

