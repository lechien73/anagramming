def get_dictionary(dictionary_file):
    with open(dictionary_file) as f:
        return [w.strip().lower() for w in f]

def count_letters(word):
    counts = {}
    for letter in word:
        counts[letter] = counts.get(letter, 0) + 1
    return counts

def anagram(a, b):
    print("Anagramming %s" % a)
    anagrams = []
    letters_dict = count_letters(a.lower())
    for word in b:
        if len(word) == len(a) and letters_dict == count_letters(word):
            anagrams.append(word.lower())
    return anagrams if anagrams else ["No single word anagrams found"]        

mydict = get_dictionary('words.txt')

print("Single Word Anagrammer")

word = input("Enter a string: ")

for anagram in anagram(word, mydict):
    print(anagram)