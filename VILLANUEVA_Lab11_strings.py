wordList = []
anotherList = []

for x in range(10):
    word = input("Enter word: ")
    wordList.append(word)

letterCount = int(input("Enter a number between 1-10: "))
print()

if letterCount <= 0 or letterCount >= 11:
    print("Invalid input. Please enter a number between 1-10.")
else:
    for word in wordList:
        if len(word) == letterCount:
            anotherList.append(word)

    if anotherList:
        print("Words with " + str(letterCount) + " letters: " + str(anotherList))
    else:
        print("There are no words found with " + str(letterCount) + " letters.")