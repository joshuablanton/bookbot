def word_count(string):
    words = []
    words = string.split()
    return len(words)

def get_character_count(string):
    chars = {}
    for i in range(0, len(string)):
        if not (string[i].lower() in chars):
            chars[string[i].lower()] = 1
        else:
            chars[string[i].lower()] += 1
    return chars

def sort_char_count(char_count):
    char_list = []
    for char in char_count:
        if char.isalpha():
            char_list.append({"char": char, "num": char_count[char]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(dict):
    return dict["num"]