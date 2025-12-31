def get_num_words(text):
    words = text.split()
    return len(words)

def get_letter_frequency(text):
    letter_dict = {}
    for ch in text.lower():
        letter_dict[ch] = letter_dict.get(ch,0) + 1
    return letter_dict

def get_char_counts(get_letter_frequency):
    chars = []
    for ch, num in get_letter_frequency.items():
        chars.append({"char": ch, "num":num})

    def sort_on(d):
        return d["num"]

    chars.sort(reverse=True, key=sort_on)
    return chars