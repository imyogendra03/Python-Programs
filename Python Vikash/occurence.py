# first occurence in the string print
s= input()
char_prev = ""
for char in s:
    if char == char_prev and char.isalnum():
        print(char)
        exit()
    char_prev = char
print(-1)

