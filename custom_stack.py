def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """

    stack = []

    # mapping closing → opening
    pairs = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for char in s:
        # If it's an opening bracket, push to stack
        if char in "([{":
            stack.append(char)

        # If it's a closing bracket
        elif char in ")]}":
            # If stack is empty → invalid
            if not stack:
                return False

            # Check if top matches expected opening
            top = stack.pop()
            if pairs[char] != top:
                return False

    # valid only if nothing left unmatched
    return len(stack) == 0