def detect(original: str, shifted: str):
    orI = 0

    for j in range(0, len(original)):
        for i in range(0, len(shifted)):
            if shifted[i] == original[j]:
                if (gather(original, shifted, i)):
                    return True

    return False

def gather(original: str, shifted: str, start: int):
    circled = []

    for i in range(start, len(shifted)):
        circled.append(shifted[i])
    
    for i in range(0, start):
        circled.append(shifted[i])

    return ''.join(circled) == original

original = "ACTGACG"
shifted = "TGACGAC"

print(detect(original, shifted))