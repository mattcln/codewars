from the_deaf_rats_of_hamelin import count_deaf_rats


def test_ex1():
    assert count_deaf_rats("~O~O~O~O P") == 0


def test_ex2():
    assert count_deaf_rats("P O~ O~ ~O O~") == 1


def test_ex3():
    assert count_deaf_rats("~O~O~O~OP~O~OO~") == 2
