import math


def train_naive_bayes(documents, labels, alpha=1.0):
    # Calculate class priors
    label_counts = {}
    total_docs = len(documents)
    for label in labels:
        label_counts[label] = label_counts.get(label, 0) + 1

    class_priors = {label: count / total_docs for label, count in label_counts.items()}

    # Count words in each class
    word_counts = {}
    total_words = {}

    for doc, label in zip(documents, labels):
        if label not in word_counts:
            word_counts[label] = {}
            total_words[label] = 0

        for word in doc.split():
            word_counts[label][word] = word_counts[label].get(word, 0) + 1
            total_words[label] += 1

    # Get vocabulary size
    vocabulary = set()
    for doc in documents:
        for word in doc.split():
            vocabulary.add(word)

    vocab_size = len(vocabulary)

    # Return the model
    return {
        'class_priors': class_priors,
        'word_counts': word_counts,
        'total_words': total_words,
        'vocabulary_size': vocab_size,
        'alpha': alpha
    }


def classify(document, model, log_space=True):
    alpha = model['alpha']
    vocab_size = model['vocabulary_size']

    scores = {}
    for label in model['class_priors']:
        # Start with the prior (in log space if specified)
        if log_space:
            scores[label] = math.log(model['class_priors'][label])
        else:
            scores[label] = model['class_priors'][label]

        # Add word likelihoods
        for word in document.split():
            word_count = model['word_counts'][label].get(word, 0)
            word_prob = (word_count + alpha) / (model['total_words'][label] + alpha * vocab_size)

            if log_space:
                scores[label] += math.log(word_prob)
            else:
                scores[label] *= word_prob

    # Return the class with highest score
    return max(scores, key=scores.get)

# Sample training data
documents = [
    "buy cheap viagra now",       # spam
    "limited time offer buy now", # spam
    "meet me at the cafe",        # ham
    "let's have lunch tomorrow"   # ham
]
labels = ["spam", "spam", "ham", "ham"]

# Train the model
model = train_naive_bayes(documents, labels)

# Test documents
test_docs = [
    "buy viagra now",     # likely spam
    "lunch at the cafe",  # likely ham
    "limited lunch offer" # ambiguous
]

# Classify test documents
for doc in test_docs:
    prediction = classify(doc, model)
    print(f"Document: '{doc}' => Predicted: {prediction}")