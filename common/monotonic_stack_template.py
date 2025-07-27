def next_greater_element(arr: List[int]) -> List[int]:
    n = len(arr)
    res = [-1] * n
    stack: List[int] = []
    
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            prev = stack.pop()
            res[prev] = arr[i]
        stack.append(i)

    return res
