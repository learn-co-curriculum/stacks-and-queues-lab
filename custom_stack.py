def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """

    stack = []

    matching_pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        if char in "([{":
            stack.append(char)

        elif char in ")]}":
            if not stack or stack[-1] != matching_pairs[char]:
                return False

            stack.pop()

    # Stack must be empty if all brackets were balanced
    return len(stack) == 0