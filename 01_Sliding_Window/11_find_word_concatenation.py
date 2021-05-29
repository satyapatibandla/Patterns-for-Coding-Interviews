from collections import Counter


# Time O(N*M*Len) | Space O(M+N)
# Where N is the number of characters in the string, M is the total number of words, and Len is the length of a word.
def find_word_concatenation(s, words):
    if not words or not words[0]:
        return []
    result_indices = []
    word_freq = Counter(words)
    num_words = len(words)
    word_len = len(words[0])
    for i in range((len(s) - num_words * word_len) + 1):
        words_seen = Counter()
        for j in range(num_words):
            next_word_index = i + j * word_len
            prospective_word = s[next_word_index:next_word_index + word_len]
            if prospective_word not in word_freq:
                break
            words_seen[prospective_word] += 1
            if words_seen[prospective_word] > word_freq.get(prospective_word, 0):
                break
            if j + 1 == num_words:
                result_indices.append(i)
    return result_indices


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


if __name__ == '__main__':
    main()
