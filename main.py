

from deep_translator import GoogleTranslator

def translate(text, language):
    languages = {
        "spanish": "es",
        "hindi": "hi"
    }

    if language.lower() not in languages:
        return "Unsupported language."

    return GoogleTranslator(
        source="en",
        target=languages[language.lower()]
    ).translate(text)


if __name__ == "__main__":
    text = input("Enter English text: ")

    print("\nChoose a language:")
    print("1. Spanish")
    print("2. Hindi")

    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        result = translate(text, "spanish")
        print("\nSpanish:", result)
    elif choice == "2":
        result = translate(text, "hindi")
        print("\nHindi:", result)
    else:
        print("Invalid choice.")