import gtts


def read_from_line():
    global words_bank
    f = open("episode8/translate.txt", "r")

    temp = f.read().split("\n")

    words_bank = []
    for i in range(0, len(temp), 2):
        my_dict = {'en': temp[i], 'fa': temp[i+1]}
        words_bank.append(my_dict)

    f.close()


def translate_en_to_fa():
    global translated
    translated = []

    user_text = input("Enter your english text: ")
    line = user_text.strip(".")
    user_words = line.split(" ")

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["en"]:
                print(word["fa"], end=" ")
                translated.append(word["fa"])
                break
        else:
            print(user_word, end=" ")

    output = str(translated)
    voice = gtts.gTTS(output, lang="ar", slow=False)
    voice.save("episode8/voice.mp3")

    print()


def translate_fa_to_en():
    translated = []

    user_text = input("Enter your english text: ")
    line = user_text.strip(".")
    user_words = line.split(" ")

    for user_word in user_words:
        for word in words_bank:
            if user_word == word["fa"]:
                print(word["en"], end=" ")
                translated.append(word["en"])
                break
        else:
            print(user_word, end=" ")

    output = str(translated)
    voice = gtts.gTTS(output, lang="en", slow=False)
    voice.save("episode8/voice.mp3")

    print()


def add_word():
    f = open("episode8/translate.txt", "a")
    en_word = input("enter english word: ")
    fa_word = input("enter persian word: ")
    f.write("\n")
    f.write(en_word)
    f.write("\n")
    f.write(fa_word)
    print("add successful✅")


def show_menu():
    print("\nwelcome\n1.translate en to fa.\n2.translate fa to en.\n3.add a new word.\n4.exit.")


while True:
    show_menu()
    read_from_line()

    user_input = input("Enter your choice: ")
    if user_input == "1":
        translate_en_to_fa()
    elif user_input == "2":
        translate_fa_to_en()
    elif user_input == "3":
        add_word()
    elif user_input == "4":
        break

print("my pleasure to chose my translate.")
