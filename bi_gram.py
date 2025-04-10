

# Count word frequencies
def count_bigrams(text):
    words = ["<s>"] + text.split() + ["</s>"]
    unigram_counts = {}
    bigram_counts = {}

    for i in range(len(words)):
        # Count unigrams
        if words[i] in unigram_counts:
            unigram_counts[words[i]] += 1
        else:
            unigram_counts[words[i]] = 1

        # Count bigrams
        if i < len(words) - 1:
            bigram = (words[i], words[i + 1])
            if bigram in bigram_counts:
                bigram_counts[bigram] += 1
            else:
                bigram_counts[bigram] = 1

    return unigram_counts, bigram_counts


# Calculate probabilities
def bigram_probability(word1, word2, unigram_counts, bigram_counts, vocabulary_size, k=0.1):
    bigram = (word1, word2)

    # Apply add-k smoothing
    numerator = bigram_counts.get(bigram, 0) + k
    denominator = unigram_counts.get(word1, 0) + k * vocabulary_size

    return numerator / denominator

