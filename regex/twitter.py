import re


def main():
    url = input("URL: ").strip()
    usename = re.sub(r"^(?:https://)?(?:www\.)?twitter\.com/", "", url)
    print(f"Username: {usename}")


if __name__ == "__main__":
    main()


