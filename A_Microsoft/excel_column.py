class Solution:
    def convert_to_title(self, num):
        capitals, res = [chr(x) for x in range(ord('A'), ord('Z') + 1)], []

        while num:
            res.append(capitals[(num - 1) % 26])
            num = (num - 1) // 26

        res.reverse()

        return ''.join(res)
