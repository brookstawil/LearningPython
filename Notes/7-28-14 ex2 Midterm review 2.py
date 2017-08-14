#7/28/14
#Midterm review
#Read in a word and count the vowels


def inspect_vowels():
    user_word = input("Give me a word! ")
    user_word = user_word.upper()
    vowel_count = 0
    last_char_was_a_vowel = False #We begin with the condition as false
    for letter in user_word: #Remember, 'in <string> will check every character in the string'
        print(letter)
    #    if (letter == "A"
    #    or letter == "E"
    #    or letter == "I"
    #    or letter == "O"
    #    or letter == "U"):
    #        vowel_count += 1

        if letter in ["A","E","I","O","U"]:
            vowel_count += 1

            if last_char_was_a_vowel:
                count_vowel_pair += 1

    return (vowel_count)

def main():
    num_vowels = inspect_vowels()
    print("There are",num_vowels,"vowels in that word")

main()
