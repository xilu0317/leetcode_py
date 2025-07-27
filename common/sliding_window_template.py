def longest_unique_substring(s: str) -> int:
    chars = set()
    res = 0
    start = 0
    
    for end in range(len(s)):
        while s[end] in chars:           # if constraint violated (repeat char)
            chars.remove(s[start])
            start += 1
        chars.add(s[end])
        res = max(res, end - start + 1)

    return res
