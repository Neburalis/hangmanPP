import random
from rows import *


def get_words_from_file(filename):
    """

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
    mask = ''
    for letter in word:
        if letter.lower() in answers:
            mask += f'{letter} '
        else:
            mask += '_ '
    return mask.strip()


def all_letters_in_set(word: str, st: set) -> bool:
    for letter in word:
        if not letter.lower() in st:
            return False
    return True


def game(word: str):
    # print(word)
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
                    print(won_message.format(word, tries))
                    break
                else:
                    if letter in word:
                        pass
                    else:
                        stage += 1
    else:
        print(gallows_stages[stage].format(mask, answers))
        print(lost_message.format(word))


def main():
    words = get_words_from_file("words.txt")
    while True:
        print(start_message)
        start_command = input().strip().lower()
        if start_command == "n":
            word = random.choice(words)
            game(word)
        elif start_command == "e":
            break
        else:
            continue


if __name__ == '__main__':
    main()
