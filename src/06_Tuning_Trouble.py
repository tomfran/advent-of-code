from utils.api import get_input

input_str = get_input(6).strip()

# answer one
for i in range(len(input_str) - 4):
    if len(set(input_str[i : i + 4])) == 4:
        print(i + 4)
        break

# answer two
for i in range(len(input_str) - 14):
    if len(set(input_str[i : i + 14])) == 14:
        print(i + 14)
        break
