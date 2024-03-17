from typing import Dict

lang_dict = {1 : "English", 2 : "Spanish", 3 : "Portuguese"}

name_prompt_dict = {1 : "What is your name?", 2 : "¿Cómo te llamas?", 3 : "Qual é o seu nome?"}

greetings_dict = { 1 : "Hello", 2 : "Hola", 3 : "Ola"}

mode_dict = {1 : "User Mode", 2 : "Admin Mode"}

admin_dict = {"Y" : "Yes", "N" : "No"}

new_language = " "


def print_mode_options(mode_options: Dict[int, str]) -> None:
    for key in mode_options:
        print(str(key) + ":", mode_options[key])


def choose_mode()-> int:
    mode_choice = input("Welcome to The Multilingual Greeter.\n" "For User Mode press 1\n" "For Admin Mode press 2\n" "To exit, hit any key.")
    return int(mode_choice)


def choose_mode_is_valid(mode_dict: Dict[int, str], mode_choice: int) -> bool:
    found_key = False
    for key in mode_dict:
        if mode_choice == key:
            found_key = True
    return found_key


def print_admin_options(admin_dict: Dict[str, str])-> None:
    for key in admin_dict:
        print(str(key) + ":", admin_dict[key])


def admin_greeter()-> None:
    new_lang_choice = input("You have entered Admin Mode.\n" "Would you like to add a language to the Greeter?\n" "Y/N")
    if (new_lang_choice.upper()) == "N":
        choose_mode()
    else:
        language_adder()



def exit_greeter(str)->None:
    print("Thank you for using The MultiLingual Greeter! Goodbye.")
    exit()



def language_adder():
    new_key = len(lang_dict) + 1
    new_language = input("What language would you like to add to the Greeter Directory?")
    lang_dict[new_key] = new_language


def name_adder():
    new_key = len(name_prompt_dict) + 1
    name_request = input("Please type \"What is your name?\" in " + new_language + ":")
    name_prompt_dict[new_key] = name_request


def greeting_adder():
    new_key = len(greetings_dict) + 1
    greeting_request = input("Please type \"Hello\" in " + new_language + ":")
    greetings_dict[new_key] = greeting_request


def exit_admin():
    print("Thank you for using Admin Mode.\n" "Returning you to the main menu:")
    print_mode_options()
    choose_mode()


def print_language_options(lang_options: Dict[int, str]) -> None:
    for key in lang_options:
        print(str(key) + ":", lang_options[key])


def language_input() -> int:
    choice = input('Choose a language:')
    return int(choice)


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    found_key = False
    for key in lang_options:
        if lang_choice == key:
            found_key = True
    return found_key


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    ask_name = name_prompt_options[lang_choice]
    return ask_name


def name_input(name_prompt: str) -> str:
    name = input(name_prompt)
    return name


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    greeting = greetings_options[lang_choice]
    print(greeting + " " + name)


if __name__ == '__main__':

def multilingual_greet_menu():
    print_mode_options(mode_dict)
    chosen_mode = choose_mode()
    while choose_mode_is_valid(mode_dict, chosen_mode) is False:
        exit_greeter()
    if chosen_mode == 1:
        user_mode()
    elif chosen_mode == 2:
            admin_mode()

def user_mode():
    print_language_options(lang_dict)
    chosen_lang = language_input()
    while language_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = language_input()

    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)


def admin_mode():
    pass
