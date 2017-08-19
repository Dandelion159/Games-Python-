#BackWord

word = input("Enter the word: ")
#создаем переменную, которая будет содержать слово наоборот
back = ""
while word != "":
    last = len(word) - 1
    last_symbol = word[last]
    back += last_symbol
    word = word[:last]
print("This is your new word: ", back)

input("\n\nPress ENTER to EXIT.")
