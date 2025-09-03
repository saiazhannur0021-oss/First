from scr.main import file_open

def test_correct_file():
    result = file_open("../pytester.txt")
    assert result == "correct"