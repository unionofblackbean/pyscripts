import name


def main():
    with open("names.txt", "r", encoding="utf8") as names_file:
        names = names_file.read().splitlines()

    valid_names = []
    for name_ in names:
        if name_:
            if name.validate_format(name_):
                valid_names.append(name_)

    with open("valid_names.txt", "w", encoding="utf8") as valid_names_file:
        for valid_name in valid_names:
            valid_names_file.write(f"{valid_name}\n")


if __name__ == "__main__":
    main()
