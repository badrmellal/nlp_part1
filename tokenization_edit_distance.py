from nltk.metrics.distance import edit_distance

def spell_check(text, dictionary):
    tokens = text.split()
    print(tokens)

    suggestions = []
    for token in tokens:
        if token in dictionary:
            continue

        # Find closest words by edit distance
        closest_words = []
        for word in dictionary:
            distance = edit_distance(token.lower(), word)
            if distance <= 2:  # max edit distance
                closest_words.append((word, distance))

        closest_words.sort(key=lambda x: x[1])
        suggestions.append((token, [word for word, _ in closest_words[:3]]))

    return suggestions


dictionary = {"hello", "world", "python", "mom", "badr", "language"}
text = "helo m pytyn"

result = spell_check(text, dictionary)

for wrong_word, guesses in result:
    print(f"Suggestions for '{wrong_word}': {guesses}")
