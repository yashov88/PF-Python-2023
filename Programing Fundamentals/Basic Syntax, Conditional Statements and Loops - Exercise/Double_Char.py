while True:
    line = input()
    if line == "End":
        break

    if line == "SoftUni":
        continue

    #converted_line = ""
    for ch in line:
        #converted_line += 2 * ch
        print(f"{ch}{ch}", end="")

    print()
    #print(converted_line)