"""This is the main module for the Stranded game."""

from db import Database
from prompts import Prompt


def main():
    print('Starting main')
    db = Database()
    prompt = Prompt(db)
    prompt.print_state()

    while True:
        print('Insert `quit` to exit the game.')
        prompt.get_prompt()
        prompt.print_state()
        print(prompt.prompt['prompt'])

        if prompt.prompt['has_answers'] == 0:
            user_input = input('Hit enter to continue... ')
        else:
            prompt.get_answers()
            prompt.print_state()
            for key, answer in prompt.answers.items():
                print(type(answer['num']), answer['num'], answer['answer'])
            user_input = input('')
            if prompt.valid_answer(user_input):
                print('User input is valid')
                # prompt.set_next_prompt(int(user_input))
                prompt.set_next_prompt(prompt.answers[int(user_input)]['following'])

        if user_input == 'quit':
            break

        prompt.print_state()
        print()

    print('Exit game!')


if __name__ == '__main__':
    print('Starting game')
    main()
