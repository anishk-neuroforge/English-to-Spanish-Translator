"""
Simple English to Spanish Translator
--------------------------------------
Requires: deep-translator
Install with: pip install deep-translator
"""

from deep_translator import GoogleTranslator


def translate_to_spanish(text: str) -> str:
    """Translate English text to Spanish."""
    return GoogleTranslator(source="en", target="es").translate(text)


def main():
    print("=== English to Spanish Translator ===")
    print("Type 'quit' or 'exit' to stop.\n")

    while True:
        text = input("Enter English text: ").strip()

        if text.lower() in ("quit", "exit"):
            print("Goodbye!")
            break

        if not text:
            continue

        try:
            translated = translate_to_spanish(text)
            print(f"Spanish: {translated}\n")
        except Exception as e:
            print(f"Error translating text: {e}\n")


if __name__ == "__main__":
    main()
