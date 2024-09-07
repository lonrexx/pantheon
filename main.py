import argparse
import sys

def read_file(path_to_files):
    info = []

    # 1234,qpoeiasid,1,1,asd,adzxc,asdqw
    # 123:zxc:d
    # 1234:zxc:asd:qwe:try:zbcvb:sadf:asdasd::asd

    for path_to_file in path_to_files:
        with open(path_to_file, mode="r") as file:
            lines = file.readlines()

            for line in lines:
                line = line.strip().split(":")

                if len(line) == 5:
                    info.append(line)
                else:
                    info.append(['incorrect line format'])

    return info 



def generate_username_from_line(info_line):
    # 
    # Maxja
    # 

    if "incorrect file format" not in info_line:
        first_name = info_line[1]
        second_name = info_line[2]
        last_name = info_line[3]

        username = ""

        if first_name != "" and second_name != "" and last_name != "":
            username = f"{first_name[0]}{second_name[0]}{last_name}"
        elif first_name != "" and last_name != "":
            username = f"{first_name[0]}{last_name}"
        elif second_name != "" and last_name != "":
            username = f"{second_name[0]}{last_name}"
        elif last_name != "":
            username = f"{last_name}"
        else:
            raise ValueError("last_name должен быть")

        if len(username) <= 8:
            return username.lower()
        elif len(username) > 8:
            return username[0:8].lower()
    
    
# print(generate_username(["1234", "", "Miloslav", "Hurban", "Legal"]))

def generate_username_from_list(info, path_to_output_file):

    # ["1234", "", "Miloslav", "Hurban", "Legal"]
    new_info = []
    
    for line in info:
        new_info.append(generate_username_from_line(line))

    new_info.reverse()

    for username in new_info:
        if username is not None and new_info.count(username) > 1:
            # new_info.index(username)
            for i in range(new_info.count(username) - 1, 0, -1):
                idx = new_info.index(username)

                new_info[idx] = username + str(i)

    new_info.reverse()

    for i, line in enumerate(info):
        if line != ['incorrect line format']:
            line.insert(1, new_info[i])

    with open(path_to_output_file, "w") as file:
        for line in info:
            if line != ['incorrect line format']:
                file.writelines(f"{':'.join(line)}\n")
            else:
                file.writelines(f"{line}\n")

# generate_username_from_list(read_file("file2.txt"))


def main():
    parser = argparse.ArgumentParser(description='Generate usernames from input files.')
    parser.add_argument('-o', '--output', required=True, help='Output file')
    parser.add_argument('input_files', nargs='+', help='Input files')

    try:
        args = parser.parse_args()

        if not args.output or not args.input_files:
            parser.print_help()
            sys.exit(1)

        print(args.input_files)
        generate_username_from_list(info=read_file(args.input_files), path_to_output_file=args.output)

    except Exception as e:
        print(e, file=sys.stderr)

        parser.print_help()
        sys.exit(1)

if __name__ == '__main__':
    # main()
    generate_username_from_list(info=read_file(["files/test_files/file3.txt", "files/test_files/file4.txt", "files/test_files/file5.txt", "files/test_files/file6.txt"]), path_to_output_file="output.txt")