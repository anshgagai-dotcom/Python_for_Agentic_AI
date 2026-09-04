# Ek function likho with list[str] parameter aur dict[str, int] return type.
# Write a function that takes a list[str] parameter and returns a dict[str, int].


def word_lengths(words: list[str]) -> dict[str, int]:
    result = {}

    for word in words:
        result[word] = len(word)

    return result


print(word_lengths(["apple", "cat", "python"]))

