def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # Map each closing bracket to its matching opening bracket
    pairs = {')': '(', ']': '[', '}': '{'}
    opening = set(pairs.values())
    stack = []

    for char in s:
        if char in opening:
            # Push opening brackets onto the stack
            stack.append(char)
        elif char in pairs:
            # For a closing bracket, the stack must not be empty and the
            # top of the stack must match the corresponding opening bracket
            if not stack or stack.pop() != pairs[char]:
                return False
        # Any other character is ignored

    # Valid only if every opening bracket was matched and closed
    return len(stack) == 0