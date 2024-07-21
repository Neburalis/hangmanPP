import random
from rows import *

words = []
with open("words.txt", 'r') as file:
    for line in file:
        words.append(line.strip())


def mask_generate(word: str) -> str:
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


if __name__ == '__main__':
    game = True

    while game:
        print(start_message)
        start_command = input()
        if start_command.strip().lower() == "n":
            game = True
        elif start_command.strip().lower() == "e":
            game = False
            break
        else:
            continue
        word = random.choice(words).strip().lower()  # in case the words data is crooked
        # print(word)
        answers = set()
        mask = mask_generate(word)
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
                if letter in answers:  # If you enter the same letter again, it will not be counted as an error.
                    pass
                else:
                    answers.add(letter)
                    mask = mask_generate(word)
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
