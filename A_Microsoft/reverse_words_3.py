class Solution:
    def reverse_words(self, s):
        res = []
        for word in s.split():
            # word[::-1] reverses the word
            res.append(word[::-1])

        return ' '.join(res)
