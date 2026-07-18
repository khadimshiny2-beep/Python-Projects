def count_words_and_characters(text):
    words = text.split()
    word_count = len(words)
    character_count = len(text)
    return word_count, character_count


def main():
    try:
        print("============== WORD COUNT PROGRAM==============")
        file = input("Give us the name of the file you wanna analyze: ")
        with open(file, "r", encoding="UTF-8") as f:
            text = f.read()
        word_count, character_count = count_words_and_characters(text)
        print(f"Your file contains {word_count} words and {character_count} characters")
    except FileNotFoundError:
        print("File unavailable.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")


if __name__ == "__main__":
    main()
