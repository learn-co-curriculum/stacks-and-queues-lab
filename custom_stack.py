# def is_valid_parentheses(s: str) -> bool:
#     """
#     Return True if the string contains valid, balanced parentheses.
#     Only (), {}, and [] are considered valid.
#     """
#     # TODO: Implement stack logic to validate parentheses
#     pass


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
        # Opening brackets are pushed onto the stack
        if char in "([{":
            stack.append(char)

        # Closing brackets must match the most recent opening bracket
        elif char in ")]}":
            if not stack or stack[-1] != matching_pairs[char]:
                return False

            stack.pop()

    # Stack must be empty if all brackets were balanced
    return len(stack) == 0