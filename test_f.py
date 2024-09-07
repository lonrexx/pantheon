import ast

def parse_file(path_to_file):
    with open(path_to_file, 'r') as file:
        data = file.read()
        
        txt = data.split("#")[1:]

        input_files_base = txt[0].split("\n")
        input_files = input_files_base[1].split(" ")

        print(input_files)

        output = txt[1].split("\n")
        print(output)

        output_list = []
        for el in output[1:]:
            el = ast.literal_eval(el)

            output_list.append(el[0])

        return input_files, output_list
    
parse_file("test_data_for_test_read_file_incorrect.txt")