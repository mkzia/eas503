# Ex1
# Write a function that takes name of two gene files, 
# reads them, and returns which genes are:
# 1) In first file but not in second file
# 2) In second file but not in first file


def get_list_from_file(filename):
    lst = []
    with open(filename) as file:
        for line in file:
            if not line.strip():
                continue

            lst.append(line.strip())

    return lst


def compare_two_lists(filename1, filename2):

    list1 = get_list_from_file(filename1)
    list2 = get_list_from_file(filename2)

    return (list(set(list1)-set(list2)), list(set(list2)-set(list1)))


print(compare_two_lists('gene_list1.txt', 'gene_list2.txt'))