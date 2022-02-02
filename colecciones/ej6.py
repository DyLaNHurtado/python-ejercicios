def print_list(list):
    print("----- PRINT LIST -----")
    for i in list:
        for j in i:
            print(j)

def set_and_print_list(list):
    print("----- SET AND PRINT LIST -----")
    for i in list:
        for j in i:
            if(j>50):
                j=0
            print(j)
    print(list)

list = [[50,34,70,20], [5,70,30,25], [10,5], [75,43,56,32,89], [54,72]]
print_list(list)
set_and_print_list(list)

