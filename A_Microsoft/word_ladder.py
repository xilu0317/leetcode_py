from collections import deque


class Solution(object):
    def ladder_length(self, begin_word, end_word, word_list):
        word_set = set(word_list)
        alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]

        q = deque([(begin_word, 1)])
        while q:
            word, length = q.popleft()
            if word == end_word:
                return length

            for i in range(len(word)):
                for c in alphabet:
                    next_word = word[:i] + c + word[i + 1:]
                    if next_word in word_set:
                        word_set.remove(next_word)
                        q.append((next_word, length + 1))

        return 0
