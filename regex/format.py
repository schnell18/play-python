import re


def main():
    name = input("What's you name? ").strip()
    # matches = re.search(r"^(.+),\s*(.+)$", name)
    # if matches:
    if matches := re.search(r"^(.+),\s*(.+)$", name):
        last, first = matches.groups()
        name = f"{first} {last}"
    print(f"Hello, {name}")


if __name__ == "__main__":
    main()


