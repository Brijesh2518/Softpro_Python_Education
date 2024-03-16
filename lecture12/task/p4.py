# find the longest common sufix substring from any list of string

def longest_common_suffix(strings):
    if not strings:
        return ""
    strings.sort()
    first = strings[0]
    last = strings[-1]
    min_len = min(len(first), len(last))
    result = ""
    for i in range(min_len):
        if first[i] == last[i]:
            result += first[i]
        else:
            break
    return result
strings = ["hello", "world", "python"]
print(longest_common_suffix(strings))
