from typing import Dict

lang_dict = {1 : "English", 2 : "Spanish", 3 : "Portuguese"}

name_prompt_dict = {1 : "What is your name?", 2 : "¿Cómo te llamas?", 3 : "Qual é o seu nome?"}

greetings_dict = { 1 : "Hello", 2 : "Hola", 3 : "Ola"}

mode_dict = {0: "Exit", 1 : "User Mode", 2 : "Admin Mode"}

new_language = " "


#def print_mode_options(mode_options: Dict[int, str]) -> None:
#    for key in mode_options:
#        print(str(key) + ":", mode_options[key])

#TODO test
def choose_mode()-> int:
    mode_choice = input("Welcome to The Multilingual Greeter.\n" "For User Mode press 1\n" "For Admin Mode press 2\n" "To exit, press 0\n>> ")
    return int(mode_choice)


def dictionary_choice_is_valid(dict: Dict[int, str], choice: int) -> bool:
    found_key = False
    for key in dict:
        if choice == key:
            found_key = True
    return found_key


def admin_greeter()-> int:
    new_lang_choice: str = input("You have entered Admin Mode.\n" "Would you like to add a language to the Greeter?\n" "Y/N\n>> ")
    if new_lang_choice.upper() == 'N':
        return 0
    elif new_lang_choice.upper() == 'Y':
        return 1
    else:
        print("Invalid choice. Please enter Y or N.")
        admin_greeter()


def exit_greeter()->None:
    print("Thank you for using The MultiLingual Greeter! Goodbye.")
    exit()

#TODO test
def language_adder():
    new_key = len(lang_dict) + 1
    new_language = input("What language would you like to add to the Greeter Directory?")
    lang_dict[new_key] = new_language
    name_request = input("Please type \"What is your name?\" in " + new_language + ":")
    name_prompt_dict[new_key] = name_request
    greeting_request = input("Please type \"Hello\" in " + new_language + ":")
    greetings_dict[new_key] = greeting_request


def exit_admin_message():
    print("Thank you for using Admin Mode.\n" "Returning you to the main menu:")
    #print_mode_options()
    #choose_mode()


def print_language_options(lang_options: Dict[int, str]) -> None:
    for key in lang_options:
        print(str(key) + ":", lang_options[key])


def language_input() -> int:
    choice = input('Choose a language:')
    return int(choice)


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    ask_name = name_prompt_options[lang_choice]
    return ask_name


def name_input(name_prompt: str) -> str:
    name = input(name_prompt)
    return name


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    greeting = greetings_options[lang_choice]
    print(greeting + " " + name)


def user_mode():
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while dictionary_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)


def admin_mode():
    #print_admin_options(admin_dict)
    response = admin_greeter()
    if response == 0:
        return
    elif response == 1:
        language_adder()

    exit_admin_message()
    return


if __name__ == '__main__':
    while True:
        mode_choice = choose_mode()
        if not dictionary_choice_is_valid(mode_dict, mode_choice):
            continue
        if mode_choice == 1:
            user_mode()
        elif mode_choice == 2:
            admin_mode()
        elif mode_choice == 0:
            exit_greeter()




