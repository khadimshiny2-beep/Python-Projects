from colorama import Fore, Back, init

init(autoreset=True)

def print_coloured_message(fore_color,back_color,message):
    print(fore_color + back_color + message)

def main():
    print("==================== Print Colored Text ====================")
    print("Demostraton")
    print_coloured_message(Fore.BLACK , Back.CYAN , "Black font on a cyan background")
    print_coloured_message(Fore.YELLOW , Back.RED , "yellow font on a red background")
    print_coloured_message(Fore.WHITE , Back.GREEN , "white font on a green background")
    print_coloured_message(Fore.BLACK , Back.WHITE , "Leave a Star on my repo!")
    print("Read the previous message again")


if __name__ == "__main__":
    main()