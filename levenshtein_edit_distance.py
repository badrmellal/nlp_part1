import Levenshtein

def spell_check(text, dictionary):
    tokens = text.split()
    suggestions = []

    for token in tokens:
        if token in dictionary:
            continue

        # Calculate edit distance to each word in dictionary
        closest_words = []
        for word in dictionary:
            distance = Levenshtein.distance(token.lower(), word)
            closest_words.append((word, distance))

        # Sort and get top 3 suggestions
        closest_words.sort(key=lambda x: x[1])
        suggestions.append((token, closest_words[:3]))

    return suggestions


dictionary = {"hello", "world", "python", "mom", "badr", "language"}
text = "helo m pytyn"

result = spell_check(text, dictionary)

for wrong_word, guesses in result:
    print(f"Suggestions for '{wrong_word}': {[word for word, dist in guesses]}")
