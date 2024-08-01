#******************************************************************************
# Author:           Nathanael Allen
# Lab:              Lab 6
# Date:             7/20/24
# Description:      This program access a database of names and their 
#                   popularity by year. 
# Output:           A table with the most common names by year
#******************************************************************************


from Name import Name

def main():
    # Gets the list of Name objects by calling showNames from the Name class
    names = Name.showNames()
    # Prints the headers
    print(f'YEAR{" " * 4}NAME{" " * 30}GENDER{" " * 8}COUNT')
    print('_' * 62)
    # prints the data
    for name in names:
        print(f'{name.getYear()}{" " * 4}{name.getName()}{" " * (36 - len(name.getName()))}{name.getGender()}{" " * 11}{name.getCount()}')

# checks if the name of the file is main and then runs the main function.
if __name__ == '__main__':
    main()