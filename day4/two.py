
def has_two_adjacent_numbers(n):
    digits = list(map(int, str(n)))
    for i in range(0, len(digits)):
        if i+1 < len(digits) and (digits[i] == digits[i+1]) \
                and (i+2 >= len(digits) or digits[i] != digits[i+2]) \
                and (i-1 < 0 or digits[i] != digits[i-1]):
                return True
    return False


def never_decrease(n):
    return int("".join(sorted(list(str(n))))) == n


possible_pwds = []
for num in range(357253, 892942):
    if has_two_adjacent_numbers(num) and never_decrease(num):
        possible_pwds.append(num)

print(len(possible_pwds))
