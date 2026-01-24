def check_is_balanced(text):
    text = text.upper()

    count_r = text.count("R")
    count_j = text.count("J")
    print(f"count_r: {count_r} count_j: {count_j}")
    return count_j == count_r


check_is_balanced("rrrrRRJJJJWLKAJIDAJWLJKWJJKJWEJJRJJEJEJEJKWJEKWJKewj")
