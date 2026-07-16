def email_slicer(email):
    try:
        username, domain = email.split("@")
        return username, domain
    except ValueError:
        raise ValueError("Invalid email address. Please retry")


def main():
    try:
        email = input("Give us your email address: ")
        username, domain = email_slicer(email)
        print(f"Username: {username}\nDomain: {domain}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
