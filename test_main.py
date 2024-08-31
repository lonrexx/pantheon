import pytest
from main import read_file, generate_username_from_list

def test_read_file():
    assert read_file(path_to_files=['file1.txt', 'file2.txt']) == [['1234', 'Jozef', 'Miloslav', 'Hurban', 'Legal'], 
                                      ['4567', 'Milan', 'Rastislav', 'Stefanik', 'Defence'], 
                                      ['4563', 'Jozef', '', 'Murgas', 'Development'], 
                                      ['0000', '', 'Murgas', 'Koala', 'Defence'],
                                      ['1111', 'Pista', '', 'Hufnagel', 'Sales'],
                                      ['4563', 'Pista', '', 'Hufnagel', 'Sales'],
                                      ['1131', 'Pista', '', 'Hufnagel', 'Sales'],
                                      ['4553', 'Pista', '', 'Hufnagel', 'Sales']]

    
    with pytest.raises(ValueError):
        read_file('incorrect:line:format')
    with pytest.raises(ValueError):
        read_file('1234:Too:Many:Fields:In:This:Line')


def test_create_username():
    generate_username_from_list(read_file(path_to_files=["file1.txt", "file2.txt"]), "output.txt")

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
