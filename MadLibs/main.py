def read_file():
    with open("madlibs.txt", encoding='utf-8') as textfile:
        lines = textfile.readlines()

    return lines

if __name__ == '__main__':
    lines = read_file()

    for i in range(len(lines)):
        init_pos = 0
        
        while init_pos != -1:
            init_pos = lines[i].find('_')
            if init_pos != -1:
                final_pos = lines[i].find('_', init_pos+1)
                blank = lines[i][init_pos:final_pos+1]
                user_input = input("Introduce un " + blank + ":\n")
                lines[i] = lines[i].replace(blank, user_input, 1)
    print("\nResultado:")
    print("".join(lines))
