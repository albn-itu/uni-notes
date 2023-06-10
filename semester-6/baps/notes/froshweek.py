def sum(tree, k):
    sum = 0
    # Go by k steps to find the other making up values
    while k >= 1:
        sum += tree[k]
        k -= k & -k
    return sum

def add(tree, k, x):
    # Go up by k steps to find the other making up values
    while k < len(tree):
        tree[k] += x
        k += k & -k

if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]

    compressed = {v: i+1 for i, v in enumerate(sorted(set(arr)))}
    compressed_size = len(compressed)

    tree = [0] * (compressed_size + 1) # 1 indexed array

    inversions = 0
    
    # Loop from the end of the array to the beginning, inclusive
    for i in range(len(arr)-1, -1, -1):
        value = compressed[arr[i]]

        inversions += sum(tree, value-1)

        add(tree, value, 1)

    print(inversions)

