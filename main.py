from sys import argv

print("######\twelcome to my first terminal tool######\nNote: this tool has a lot of problems sorry :)\n\n")

option = argv[1]
def find_first(arg1, arg2):
    indexing = 0
    line = 0
    li = ""
    try:
        with open(arg1, "r", encoding="utf-8") as content:
            text = content.readlines()
    except FileNotFoundError:
        print(f"Error: File '{arg1}' not found. Please check the file name and try again ")
        return ""
    except Exception:
        print("An error occurred.")
        return ""
    for lines in text:
        if arg2.lower() in text[indexing].lower():
            li = text[indexing]
            line = text.index(li)
            indexing += 1
            return f"Line {str(line + 1)}: {li.strip()}"
        else:
            indexing += 1
    return f"Word {arg2} not found in this file."

def main(option):
    if option in ["-h", "--help"]:
        print("Usage: py file.txt <option> argument1 argument2\n\noptions:\n\n-h, --help show you how to use this tool\n-f,--find show you the first time the pattren was write in you file ")
        return
    if option in ["-f", "--find"]:
        if len(argv) < 3 :
            print('Error: you need to enter file path and pattren')
            return
        else:
            file_path = argv[2]
            pattren = argv[3]
            print(grep(file_path, pattren))
            return
    else:
        print("Invalid option: try -h")
        return

if __name__ == "__main__":
    main(option)



