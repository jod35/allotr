def find_vowel(word):
    vowel_count = 0
    vowels = ""
    consonant_count = 0
    consonats = ""
    try:
        for char in word:
            if char not in "aeiouAEIOU":
                if char not in consonats:
                    consonant_count += 1

            else:
                vowel_count += 1
        print(f"Number of vowels: {vowel_count}")
        print(f"Number of consonants: {consonats}")

    except Exception as e:
        print("Something wrong happened")


find_vowel("Jonathan")
find_vowel("EXCUSE ME")
