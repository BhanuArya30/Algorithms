
def most_common_substring(s:str, k:int) -> str:
    if k > len(s):
        return ""
    substring_count = {}

    for i in range(len(s) - k + 1):
        subtring = s[i:i+k]
        substring_count[subtring] = substring_count.get(subtring, 0) + 1

    return max(substring_count, key=substring_count.get)

s = "xarbcabadbab"
# s = "aaaaaa"
k = 2
result = most_common_substring(s, k)
print(result)
print(s[s.index(result):])

