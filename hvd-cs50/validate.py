import re

# pat = re.compile(r'\w+\.?\w+@\w+\.?\w+')
pat = re.compile(r'^[a-zA-Z0-9_]\.?[a-zA-Z0-9_]+@\w+\.?\w+', re.IGNORECASE)


def main():
    email = input("What's you email? ").strip()
    m = re.match(pat, email)
    if m:
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()

