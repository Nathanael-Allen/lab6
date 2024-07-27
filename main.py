from Name import Name

def main():
    names = Name.showNames()
    print(f'YEAR{" " * 4}NAME{" " * 30}GENDER{" " * 8}COUNT')
    print('_' * 62)

    for name in names:
        print(f'{name.getYear()}{" " * 4}{name.getName()}{" " * (36 - len(name.getName()))}{name.getGender()}{" " * 11}{name.getCount()}')


if __name__ == '__main__':
    main()