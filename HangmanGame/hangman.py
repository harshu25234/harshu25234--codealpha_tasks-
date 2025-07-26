import random

# Predefined list of 5 words
word_list = ["apple", "tiger", "chair", "house", "green"]
word_to_guess = random.choice(word_list)

# Create a list of underscores for the guessed word
guessed_word = ["_"] * len(word_to_guess)
guessed_letters = []
attempts_left = 6

print("🎮 Welcome to Hangman!")
print("Guess the word letter by letter.")

# Game loop
while attempts_left > 0 and "_" in guessed_word:
    print("\nWord: " + " ".join(guessed_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts left: {attempts_left}")
    
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guessed letter is in the word
    if guess in word_to_guess:
        print("✅ Good guess!")
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
    else:
        print("❌ Incorrect guess.")
        attempts_left -= 1

# Final result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("\n💀 Game over! The word was:", word_to_guess)
