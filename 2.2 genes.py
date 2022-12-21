
FILENAME = "genetic_code.csv"


def readfile(filename):
    try:
        with open(filename) as my_file:
            my_return = []
            file = my_file.readlines()
            for lines in file:
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
    given_codons = "GUAUGCACCUCGUCGUGACUUUCCUCAUGAGCUGAUGAAGCU"
    #   GUAUGCACGUGACUUUCCUCAUGAGCUGAU
    genetic_codes = genetic_code_dict(FILENAME)

    try:
        if len(given_codons.split("GUG", 1)[1]) > len(given_codons.split("AUG", 1)[1]):
            our_codons = "GUG"+given_codons.split("GUG", 1)[1]
        else:
            our_codons = "AUG"+given_codons.split("AUG", 1)[1]
        print(our_codons)

        #   Secondly, we need to divide them to three and make a list:
        codons_list = [(our_codons[i:i + 3]) for i in range(0, len(our_codons), 3)]
        for element in codons_list:
            if len(element) != 3:
                codons_list.remove(element)
        print(codons_list)

        #   Thirdly, we need to tranform our mRNA to acid names:
        result_str = ''
        for codons in codons_list:
            for acid_names, codes in genetic_codes.items():
                for cod in codes:
                    if codons == cod:
                        result_str = result_str + acid_names

        result_str = "".join(result_str.split("start"))
        print(result_str)

    except IndexError:
        print("In mRNA there is no start codon")




if __name__ == '__main__':
    main()
