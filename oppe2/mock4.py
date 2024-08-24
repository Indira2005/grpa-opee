def most_frequent_alpha_character(filename: str) -> list:
    '''
    Arguments:
    filename: str - name of the file

    Return:
    list - the most frequent alphabetic characters (case-sensitive)
    '''
    d_cnt = {}
    with open(filename, "r") as f:
        for line in f:
            s = line.lower().strip()
            for ch in s:
                if ch.isalpha():
                    if ch in d_cnt.keys():
                        d_cnt[ch] += 1
                    else :
                        d_cnt[ch] = 1
    try:
        max_freq = max(d_cnt.values())
    except ValueError:
        return []

    most_freq_char = []
    for ch, freq in d_cnt.items():
        if freq == max_freq:
            most_freq_char.append(ch)
    
    return most_freq_char
