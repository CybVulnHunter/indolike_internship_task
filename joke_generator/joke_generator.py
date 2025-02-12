import pyjokes

def generate_random_joke(language='en'):
    try:
        joke = pyjokes.get_joke(language=language)
        print("\n" + joke + "\n")
    except Exception as e:
        print(f"Error: {e}")

def generate_multiple_jokes(count=1, language='en'):
    try:
        jokes = pyjokes.get_jokes(language=language)
        if not jokes:
            print("No jokes found for the specified language.")
            return
        for i in range(min(count, len(jokes))):
            print(f"{i + 1}. {jokes[i]}")
            print('-' * 50)
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("\nWelcome to the Joke Generator!")
    while True:
        print("\nChoose an option:")
        print("1. Generate a random joke")
        print("2. Generate multiple jokes")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            language = input("Enter the language code (default: en): ").strip() or 'en'
            generate_random_joke(language)
        elif choice == '2':
            try:
                count = int(input("Enter the number of jokes to generate: ").strip())
                language = input("Enter the language code (default: en): ").strip() or 'en'
                generate_multiple_jokes(count, language)
            except ValueError:
                print("Invalid input! Please enter a valid number for the joke count.")
        elif choice == '3':
            print("Goodbye! Have a great day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
