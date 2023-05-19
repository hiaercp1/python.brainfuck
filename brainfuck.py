def execute_brainfuck(code):
    tape = [0] * 30000
    pointer = 0
    output = ''

    i = 0
    while i < len(code):
        command = code[i]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            tape[pointer] = (tape[pointer] + 1) % 256
        elif command == '-':
            tape[pointer] = (tape[pointer] - 1) % 256
        elif command == '.':
            output += chr(tape[pointer])
        elif command == ',':
            # Implement input handling as needed
            pass
        elif command == '[':
            if tape[pointer] == 0:
                loop_count = 1
                while loop_count > 0:
                    i += 1
                    if code[i] == '[':
                        loop_count += 1
                    elif code[i] == ']':
                        loop_count -= 1
            else:
                # Store the index of the opening bracket for looping
                loop_stack.append(i)
        elif command == ']':
            if tape[pointer] != 0:
                i = loop_stack[-1] - 1
            else:
                loop_stack.pop()

        i += 1

    return output
