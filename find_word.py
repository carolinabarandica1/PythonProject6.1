def find_words(filename):
    """
    Print the 3-letter words starting with 'b'.
    :param filename: The name of the file.
    :return: Nothing.
    """

    with open(filename, 'r') as f:
        for line in f:
            # Break down the line into words
            words = line.split()
            for word in words:
                if len(word) == 3 and word.upper()[0] == "B":
                    print(word)


find_words("input_txt")