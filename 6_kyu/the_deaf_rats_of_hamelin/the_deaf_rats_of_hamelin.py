def count_deaf_rats(rats):
    nb_wrong_cat = 0
    left_rats, right_rats = rats.replace(" ", "").split("P")
    if left_rats:
        for char in range(0, len(left_rats), 2):
            if left_rats[char] != "~":
                nb_wrong_cat += 1
    if right_rats:
        for char in range(1, len(right_rats), 2):
            if right_rats[char] != "~":
                nb_wrong_cat += 1
    return nb_wrong_cat
