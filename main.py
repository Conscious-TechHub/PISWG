import random
import string

PROGRAM_VERSION = "1.0"
# Main program loop
while True:
    from pyfiglet import Figlet
    f = Figlet(font='slant')
    print(f.renderText('PISWG'))
    print("---------------------------------------------------------------------------------------")
    print(" Professional  Indian Social Media Wordlist Gernator ")
    print("---------------------------------------------------------------------------------------")
    print("\nMenu:")
    print("1.  Social Media Wordlist Generate")
    print("2.  Website Wordlist Generate")
    print("3.  Random Wordlist Generate")
    print("4.  Update Wordlists")
    print("5.  Exit")
    print("---------------------------------------------------------------------------------------")

    choice = input("Enter your Choice: ")
    print("---------------------------------------------------------------------------------------")

    if choice == '1':
        def load_words_from_file(filename):
            words = []
            with open(filename, 'r') as file:
                for line in file:
                    words.append(line.strip())
            return words

        def generate_combinations(name, words_list):
            combinations = []
            for word in words_list:
                combinations.append(name + word)
                combinations.append(word + name)
            return combinations

        def save_to_txt(filename, data_list):
            with open(filename, 'w') as file:
                for item in data_list:
                    file.write(f"{item}\n")

        # Get user input for name and filename
        name = input("Enter your Target Name: ")
        print("---------------------------------------------------------------------------------------")
        filename = input("Enter the filename to save the combinations (without extension): ") + '.txt'
        print("---------------------------------------------------------------------------------------")
        # Load words from PISWG.txt file
        words_list = load_words_from_file('PISWG.txt')

        # Generate combinations
        combinations = generate_combinations(name, words_list)

        # Save combinations to the specified filename
        save_to_txt(filename, combinations)

        # Display all generated words
        print("Generated words:")
        for word in combinations:
            print(word)
        print("---------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------")
    elif choice == '2':
        print("---------------------------------------------------------------------------------------")
        def load_words_from_file(filename):
            words = []
            with open(filename, 'r') as file:
                for line in file:
                    words.append(line.strip())
            return words

        def generate_combinations(username_list, password_list):
            combinations_username = [f"{username}{password}" for username in username_list for password in password_list]
            combinations_password = [f"{password}{username}" for username in username_list for password in password_list]
            return combinations_username, combinations_password

        def save_to_txt(filename, data_list):
            with open(filename, 'w') as file:
                for item in data_list:
                    file.write(f"{item}\n")

        # Load usernames and passwords from files
        usernames = load_words_from_file('username.txt')
        passwords = load_words_from_file('password.txt')

        # Generate combinations for web login brute-force
        combinations_username, combinations_password = generate_combinations(usernames, passwords)

        # Save combinations to separate files
        save_to_txt('username_combinations.txt', combinations_username)
        save_to_txt('password_combinations.txt', combinations_password)

        # Display the generated combinations
        print("Generated username combinations:")
        for username_combination in combinations_username:
            print(username_combination)
        print("---------------------------------------------------------------------------------------")
        print("\nGenerated password combinations:")
        for password_combination in combinations_password:
            print(password_combination)
        print("---------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------")
    elif choice == '3':
        print("---------------------------------------------------------------------------------------")
        def generate_word_list(length, num_words, char_set):
            char_set_choices = {
                'A-Z': string.ascii_uppercase,
                'a-z': string.ascii_lowercase,
                '0-9': string.digits,
            }

            if char_set not in char_set_choices:
                raise ValueError("Invalid character set choice.")

            char_set = char_set_choices[char_set]
            word_list = []

            for _ in range(num_words):
                word = ''.join(random.choice(char_set) for _ in range(length))
                word_list.append(word)

            return word_list

        def save_word_list_to_file(word_list, filename):
            with open(filename, 'w') as file:
                for word in word_list:
                    file.write(f"{word}\n")
        print("---------------------------------------------------------------------------------------")
        # Get user input for word list generation
        length = int(input("Enter the length of each word: "))
        print("---------------------------------------------------------------------------------------")
        num_words = int(input("Enter the number of words to generate: "))
        print("---------------------------------------------------------------------------------------")
        char_set = input("Choose character set (A-Z, a-z, 0-9): ")
        print("---------------------------------------------------------------------------------------")

        # Generate word list
        word_list = generate_word_list(length, num_words, char_set)

        # Get user input for file name to save the word list
        filename = input("Enter the filename to save the word list (without extension): ") + '.txt'

        # Save word list to file
        save_word_list_to_file(word_list, filename)
        print("---------------------------------------------------------------------------------------")
        print(f"Word list saved to {filename}")
        print("---------------------------------------------------------------------------------------")
    elif choice == '4':
        print("---------------------------------------------------------------------------------------")
        print("Author Name:- Vikki Verma ") 
        print(" VERSION",PROGRAM_VERSION )
        print(" Update Coming Soon " )
        
        
        print("---------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------")
    elif choice == '5':
        print("Exiting the program...")
        print("---------------------------------------------------------------------------------------")
        print("---------------------------------------------------------------------------------------")
        print("Exit")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


