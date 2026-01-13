def length_of_last_word(s: str) -> int:
    word = s.strip().split()
    return len(word[-1])
print(length_of_last_word("Hello world"))