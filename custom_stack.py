def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # Map each closing bracket to its matching opening bracket
    matching = {')': '(', ']': '[', '}': '{'}

    stack = []  # LIFO stack to track unmatched opening brackets

    for char in s:
        if char in '([{':
            # Opening bracket: push onto the stack
            stack.append(char)
        elif char in ')]}':
            # Closing bracket: stack must have a matching opener on top
            if not stack or stack[-1] != matching[char]:
                return False
            stack.pop()  # Matched — remove the opener

    # Valid only if every opener was matched and removed
    return len(stack) == 0