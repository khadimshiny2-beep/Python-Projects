def pounds_to_kg(pounds):
    return pounds * 0.453592


def main():
    pounds = int(input("Enter weight in lbs: "))
    kilos = pounds_to_kg(pounds)
    print(f"{pounds} lbs = {kilos} kg")


if __name__ == "__main__":
    main()
