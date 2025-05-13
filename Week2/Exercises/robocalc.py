def calculate(input, rules):
    # Step 1: Build the tape by adding L and R
    tape = ['L'] + list(input) + ['R']
    pos = 0         # Start at the 'L'
    state = 1       # Initial state
    steps = 0       # Step counter

    # Step 2: Convert rules to a dictionary for fast lookup
    rule_map = {}
    for current_symbol, current_state, new_symbol, new_state, action in rules:
        rule_map[(current_symbol, current_state)] = (new_symbol, new_state, action)

    # Step 3: Run up to 1000 steps
    while steps < 1000:
        current_symbol = tape[pos]
        key = (current_symbol, state)

        if key not in rule_map:
            return False  # No matching rule

        new_symbol, new_state, action = rule_map[key]
        tape[pos] = new_symbol
        state = new_state

        if action == "LEFT":
            pos -= 1
            if pos < 0:
                return False
        elif action == "RIGHT":
            pos += 1
            if pos >= len(tape):
                return False
        elif action == "ACCEPT":
            return True
        elif action == "REJECT":
            return False

        steps += 1

    return False 

if __name__ == "__main__":
    rules = []

    rules.append(("L", 1, "L", 2, "RIGHT"))
    rules.append(("L", 3, "L", 2, "RIGHT"))

    rules.append(("0", 2, "X", 4, "RIGHT"))
    rules.append(("1", 4, "X", 5, "RIGHT"))
    rules.append(("1", 2, "X", 6, "RIGHT"))
    rules.append(("0", 6, "X", 7, "RIGHT"))

    rules.append(("0", 4, "0", 4, "RIGHT"))
    rules.append(("0", 5, "0", 5, "RIGHT"))
    rules.append(("0", 7, "0", 7, "RIGHT"))
    rules.append(("1", 6, "1", 6, "RIGHT"))
    rules.append(("1", 5, "1", 5, "RIGHT"))
    rules.append(("1", 7, "1", 7, "RIGHT"))

    rules.append(("X", 2, "X", 2, "RIGHT"))
    rules.append(("X", 4, "X", 4, "RIGHT"))
    rules.append(("X", 5, "X", 5, "RIGHT"))
    rules.append(("X", 6, "X", 6, "RIGHT"))
    rules.append(("X", 7, "X", 7, "RIGHT"))

    rules.append(("R", 2, "R", 2, "ACCEPT"))
    rules.append(("R", 4, "R", 4, "REJECT"))
    rules.append(("R", 6, "R", 6, "REJECT"))

    rules.append(("R", 5, "R", 3, "LEFT"))
    rules.append(("R", 7, "R", 3, "LEFT"))
    rules.append(("0", 3, "0", 3, "LEFT"))
    rules.append(("1", 3, "1", 3, "LEFT"))
    rules.append(("X", 3, "X", 3, "LEFT"))

    print(calculate("0", rules)) # False
    print(calculate("00", rules)) # False
    print(calculate("01", rules)) # True
    print(calculate("0110", rules)) # True
    print(calculate("0101", rules)) # True
    print(calculate("1000", rules)) # False
    print(calculate("00110101", rules)) # True
    print(calculate("00111101", rules)) # False