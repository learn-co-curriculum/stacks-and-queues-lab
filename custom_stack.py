def is_valid_parentheses(s: str) -> bool:
    """
    Return True if the string contains valid, balanced parentheses.
    Only (), {}, and [] are considered valid.
    """
    # TODO: Implement stack logic to validate parentheses
    stack = []  #  store opening brackets

    # dictionary to match closing to opening brackets
    matches = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    # go through each character in the string
    for char in s:
        if char in "({[":
            # push opening brackets onto the stack
            stack.append(char)
        elif char in ")}]":
            # if there's no opening bracket to match
            if len(stack) == 0:
                return False

            # pop the last opening bracket
            top = stack.pop()

            # check if it matches the current closing bracket
            if top != matches[char]:
                return False

    # if stack is empty, all brackets were matched
    return len(stack) == 0
