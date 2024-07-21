import random
from rows import *


def get_words_from_file(filename):
    """
    function to get the word base for the game from a file
    :param filename: filename from which the word base will be obtained
    :return: words base in list
    """
    words = []
    with open(filename, 'r') as file:
        for line in file:
            words.append(line.strip().lower())
    return words


def get_words_from_other():
    """
    another implementation of getting words
    :return:
    """
    ...


def mask_generate(word: str, answers: set) -> str:
    """
    function for generating a word mask - a string in which unknown letters are hidden
    :param word: word for generating mask
    :param answers: set of known letters
    :return: generated mask
    """
    mask = ''
    for letter in word:
        if letter.lower() in answers:
            mask += f'{letter} '
        else:
            mask += '_ '
    return mask.strip()


def all_letters_in_set(word: str, st: set) -> bool:
    """
    function for checking if all letters in the word are present in the set
    :param word: word for checking
    :param st: set of known letters
    :return:
    """
    for letter in word:
        if not letter.lower() in st:
            return False
    return True


def send_won_message(word, tries) -> None:
    print(won_message.format(word, tries))


def send_lost_message(word) -> None:
    print(lost_message.format(word))


def game(word: str) -> bool:
    """
    game main function
    :param word: hidden word
    :return: True if game won, False otherwise
    """
    print(word)
    answers = set()
    mask = mask_generate(word, answers)
    stage = 0
    tries = 0

    while stage < len(gallows_stages) - 1:
        print(gallows_stages[stage].format(mask, answers))
        letter = input().strip().lower()
        tries += 1
        if letter == word:
            print(won_message.format(word, tries))
            break
        elif len(letter) == 1:
            if letter in answers:
                tries -= 1
            else:
                answers.add(letter)
                mask = mask_generate(word, answers)
                if all_letters_in_set(word, answers):
                    send_won_message(word, tries)
                    return True
                else:
                    if letter in word:
                        pass
                    else:
                        stage += 1
    print(gallows_stages[stage].format(mask, answers))
    send_lost_message(word)
    return False


def save_results(result: bool, player_name: str, filename: str) -> None:
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()

        for i, line in enumerate(lines):
            name, wins, losses = line.strip().split()
            if name == player_name:
                wins = int(wins)
                losses = int(losses)
                if result:
                    wins += 1
                else:
                    losses += 1
                lines[i] = f'{name} {wins} {losses}\n'
                break
        else:
            if result:
                lines.append(f'{player_name} 1 0\n')
            else:
                lines.append(f'{player_name} 0 1\n')
    except FileNotFoundError:
        with open(filename, 'w') as file:
            if result:
                file.write(f'{player_name} 1 0\n')
            else:
                file.write(f'{player_name} 0 1\n')


def main() -> None:
    """
    game launch function
    :return: None
    """
    words = get_words_from_file("words.txt")
    while True:
        print(start_message)
        start_command = input().strip().lower()
        if start_command == "n":
            print('What is your name?', 'This is necessary for compiling statistics')
            name = input().strip()
            word = random.choice(words)
            result = game(word)
            save_results(result, name, "results.txt")
        elif start_command == "e":
            break
        else:
            continue


if __name__ == '__main__':
    main()
