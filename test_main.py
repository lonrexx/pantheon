import pytest

from main import read_file, generate_username_from_list, generate_username_from_line
from test_f import parse_file

def test_read_file():
    input_files, output_list = parse_file("test_data_for_test_read_file_correct.txt")

    assert read_file(input_files) == output_list
    
    input_files, output_list = parse_file("test_data_for_test_read_file_incorrect.txt")
    assert read_file(input_files) == output_list


def test_create_username():
    generate_username_from_list(read_file(path_to_files=["files/test_files/file1.txt", "files/test_files/file2.txt"]), "output.txt")

    with open("output.txt", 'r') as file:
        lines = file.readlines()

        assert '1234:jmhurban:Jozef:Miloslav:Hurban:Legal\n' in lines
        assert '4567:mrstefan:Milan:Rastislav:Stefanik:Defence\n' in lines
        assert '4563:jmurgas:Jozef::Murgas:Development\n' in lines
        assert '0000:mkoala::Murgas:Koala:Defence\n' in lines
        assert '1111:phufnage:Pista::Hufnagel:Sales\n' in lines
        assert '4563:phufnage1:Pista::Hufnagel:Sales\n' in lines
        assert '1131:phufnage2:Pista::Hufnagel:Sales\n' in lines
        assert '4553:phufnage3:Pista::Hufnagel:Sales\n' in lines


# def test_create_username_from_line():
#     generate_username_from_line(info_line=[])