from colorama import Fore
from random import choice


def show_grid(words_grid):
    """
    Display letters to user.
    If letter is placed correctly, shows it in green; if it is placed wrongly, shows it in yellow; if letter in not on
    secret word, shows it in red; the empty places are displayed in white.
    :param words_grid: list with nested lists with letters to be displayed
    :return: no return
    """
    for line in words_grid:
        print("  ", end="")
        for i in line:
            if i == ' _ ':
                print(Fore.WHITE + i, end="")
            elif len(i) == 3:
                print(Fore.YELLOW + ' ' + i[2] + ' ', end="")
            elif len(i) == 4:
                print(Fore.GREEN + ' ' + i[3] + ' ', end="")
            else:
                print(Fore.RED + ' ' + i + ' ', end="")
        print()
    print()


def in_used_letters(letter, used_letters):
    """

    :param letter: char to be compared with used_letters
    :param used_letters: list of letters already used by user
    :return: string with the color to be used
    """
    color = "WHITE"
    for i in used_letters:
        if len(i) == 4:
            if i[3].upper() == letter:
                return "GREEN"
        elif len(i) == 3:
            if i[2].upper() == letter:
                color = "YELLOW"
        elif i.upper() == letter:
            color = "RED"
    return color


def show_letters(used_letters):
    """
    Display QWERT letters already attempted to user.
    If letter is placed correctly, shows it in green; if it is placed wrongly, shows it in yellow; if letter in not on
    secret word, shows it in red; the unesed letters are displayed in white
    :param used_letters: list of letters already used by user
    :return: no return
    """
    letters = "QWERTYUIOPASDFGHJKLÇZXCVBNM"

    for letter in letters:
        if letter == 'P' or letter == 'Ç' or letter == 'M':
            # in_used_letters is called to define the color with which the letter will be displayed
            color = in_used_letters(letter, used_letters)
            if color == "RED":
                print(Fore.RED + ' ' + letter)
            elif color == "YELLOW":
                print(Fore.YELLOW + ' ' + letter)
            elif color == "GREEN":
                print(Fore.GREEN + ' ' + letter)
            elif color == "WHITE":
                print(Fore.WHITE + ' ' + letter)
        elif letter == 'Z':
            color = in_used_letters(letter, used_letters)
            if color == "RED":
                print(Fore.RED + '    ' + letter, end="")
            elif color == "YELLOW":
                print(Fore.YELLOW + '    ' + letter, end="")
            elif color == "GREEN":
                print(Fore.GREEN + '    ' + letter, end="")
            elif color == "WHITE":
                print(Fore.WHITE + '    ' + letter, end="")
        else:
            color = in_used_letters(letter, used_letters)
            if color == "RED":
                print(Fore.RED + ' ' + letter, end="")
            elif color == "YELLOW":
                print(Fore.YELLOW + ' ' + letter, end="")
            elif color == "GREEN":
                print(Fore.GREEN + ' ' + letter, end="")
            elif color == "WHITE":
                print(Fore.WHITE + ' ' + letter, end="")
    print()


def update_grid(attempts, word_row, words_grid, guess_sign):
    """
    Updates words_grid with letters in upper case and accent if present
    :param attempts: int with the # of the user attempt
    :param word_row: list with letters used on the guess to be included on words_grid
    :param words_grid: list with nested lists with letters to be displayed
    :param guess_sign: string with guessed word
    :return: words_grid updated
    """
    for index, letter in enumerate(word_row):
        if len(letter) == 3:
            word_row[index] = 'e_' + guess_sign[index].upper()
        elif len(letter) == 4:
            word_row[index] = 'ec_' + guess_sign[index].upper()
        else:
            word_row[index] = guess_sign[index].upper()

    words_grid[attempts - 1] = word_row
    return words_grid


def main():
    # Use a breakpoint in the code line below to debug your script.
    # Create empty grid
    words_grid = [[' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '], [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '],
                  [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '], [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '],
                  [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ '], [' _ ', ' _ ', ' _ ', ' _ ', ' _ ', ' _ ']]
    list_of_words = []
    list_of_words_no_sign = []
    dict_words_in_portuguese = {}
    used_letters = []

    attempts = 1
    word_size = 6
    won_flag = False

    opening = """
*********************************************************************************
*********************************************************************************

                                  TERMO_6
                    
*********************************************************************************
*********************************************************************************
                                COMO JOGAR
Você terá 6 tentativas. Cada uma delas deve ser uma palavra que exista.
Escreva sem acentos. Eles serão incluídos na resposta.
Após o palpite, as letras mudarão para indicar o quão perto você está da resposta.

Se uma letra ficar verde, ela está presente na palavra e na posição correta.
Se uma letra ficar amarela, ela está presente na palavra, mas na posição errada.
Se uma letra ficar vermelha, ela NÃO está na palavra.

*********************************************************************************
*********************************************************************************
    """
    print(opening)

    # read txt with words in pt-br and add 6 letters words to list
    with open("br-utf8.txt", "r", encoding="utf-8") as file:
        for line in file:
            word = line.rstrip()
            if len(word) == 6:
                list_of_words.append(word)

    # read txt with words in pt-br(no accents) and add 6 letters words to list
    with open("br-sem-acentos.txt", "r") as f:
        for line in f:
            word = line.rstrip()
            if len(word) == 6:
                list_of_words_no_sign.append(word)

    # dict where keys are words with no accent and values are the words properly written
    for index, word in enumerate(list_of_words_no_sign):
        dict_words_in_portuguese[word] = list_of_words[index]

    # choose word to be guessed
    secret_word = None
    while secret_word is None:
        secret_word_no_sign = choice(list_of_words_no_sign)
        secret_word = dict_words_in_portuguese.get(secret_word_no_sign)

    # user has 6 attempts
    while attempts <= 6:
        word_row = ['_', '_', '_', '_', '_', '_']

        # call function to display words_grid to user
        show_grid(words_grid)

        # erase repeated letters from list
        used_letters = list(set(used_letters))

        # call function to display letters already used to user
        show_letters(used_letters)

        # prompt user for guess
        guess = input(Fore.BLUE + 'Palpite #' + str(attempts) + ': ').replace('ç', 'c').lower()

        # verify if is 6 letter word with only alpha chars
        if not len(guess) == word_size:
            print("Tente de novo")
            continue
        elif not guess.isalpha():
            print("Tente de novo")
            continue

        # verify if guess exists on the dictionary
        guess_sign = dict_words_in_portuguese.get(guess)
        if not guess_sign:
            print("Tente de novo")
            continue

        # verify if letter in guess exists and is correctly placed on secret_word_no_sign
        # iterate over the guessed word and if it exists on the copy_secret_word_no_sign and is placed correctly, add
        # 'ec_' + 'letter' to word row, add used letters to list and replace letters already checked from
        # copy_secret_word_no_sign
        copy_secret_word_no_sign = list(secret_word_no_sign.lower())
        for index, letter in enumerate(guess):
            if letter in copy_secret_word_no_sign:
                if letter == secret_word_no_sign[index]:
                    word_row[index] = 'ec_' + letter
                    used_letters.append(word_row[index])
                    copy_secret_word_no_sign[index] = '0'
        # print(f"copy_secret_word_no_sign: {copy_secret_word_no_sign}")
        # print(f"word_row: {word_row}")

        # verify if letter in guess exists but is wrongly placed on secret_word_no_sign
        # iterate over the guessed word and if it exists on the copy_secret_word_no_sign, add 'e_' + 'letter' to word
        # row, add used letters to list and replace letters already checked from copy_secret_word_no_sign
        for index, letter in enumerate(guess):
            if letter in copy_secret_word_no_sign:
                if word_row[index] == '_':
                    word_row[index] = 'e_' + letter
                    used_letters.append(word_row[index])
                    for index_2, letter_2 in enumerate(copy_secret_word_no_sign):
                        if letter == letter_2:
                            copy_secret_word_no_sign[index_2] = '0'
                            break
        # print(f"copy_secret_word_no_sign: {copy_secret_word_no_sign}")
        # print(f"word_row: {word_row}")

        # verify if letter in guess do not exists on secret_word_no_sign
        # iterate over the guessed word and if it does not exists on the copy_secret_word_no_sign, add letter to word
        # row, add used letters to list
        for index, letter in enumerate(guess):
            if word_row[index] == '_':
                word_row[index] = letter
                used_letters.append(word_row[index])
        # print(f"copy_secret_word_no_sign: {copy_secret_word_no_sign}")
        # print(f"word_row: {word_row}")

        # call function to add word_row to words_grid
        words_grid = update_grid(attempts, word_row, words_grid, guess_sign)
        attempts += 1

        # if user guessed the word, stop game and raise the won_flag
        if guess == secret_word_no_sign:
            won_flag = True
            break

    # when the game is finished, display results to user
    show_grid(words_grid)
    print()

    if won_flag:
        cake = """
             ,   ,   ,   ,             
           , |_,_|_,_|_,_| ,           
       _,-=|;  |,  |,  |,  |;=-_       
     .-_| , | , | , | , | , |  _-.     
     |:  -|:._|___|___|__.|:=-  :|     
     ||*:  :    .     .    :  |*||     
     || |  | *  |  *  |  * |  | ||     
 _.-=|:*|  |    |     |    |  |*:|=-._ 
-    `._:  | *  |  *  |  * |  :_.'    -
 =_      -=:.___:_____|___.: =-     _= 
    - . _ __ ___  ___  ___ __ _ . -   
        """

        print(Fore.LIGHTGREEN_EX + "Parabéns! Você venceu!")
        print(f"{attempts - 1}/6 tentativas")
        print(cake)

    else:
        skull = """
@@@@@                                        @@@@@
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@
        """
        print(Fore.MAGENTA + "Infelizmente você perdeu. Melhor sorte na próxima vez")
        print(f"A palavra era {secret_word}")
        print(skull)


# Press the green button in the gutter to run the script.
# Inspired by Wordle and Termo, but with words in brazilian portuguese and 6 letters words
# Version 1.0 by Leandro Almeida
if __name__ == '__main__':
    main()

