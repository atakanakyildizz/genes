
FILENAME = "genetic_code.csv"
def readfile(filename):
    try:
        with open(filename) as my_file:
            my_return = []
            file = my_file.readlines()
            for lines in file:
                lines = lines.replace(" ", '')
                lines = lines.replace('"', '')
                lines = lines.replace(" ", '')
                lines = lines.replace("\n", "")
                my_return.append(lines.split(","))

    except OSError as error:
        print(f"Whops we have a problem here !!\n{error}")
        my_return = "Check the filename"
    return my_return


def genetic_code_dict(filename):
    my_text = readfile(filename)
    genetic_code = dict()

    for i in range(len(my_text)):
        templist = []
        for j in range(len(my_text[i])-1):
            templist.append(my_text[i][j+1])
            genetic_code[my_text[i][0]] = templist
    return genetic_code

def main():
    genetic_code_dict(FILENAME)


if __name__ == '__main__':
    main()
