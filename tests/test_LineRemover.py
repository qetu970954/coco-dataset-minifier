from utilities.LineRemover import LineRemover


def test_LineRemover():
    remover = LineRemover("tests/resources")
    actual = remover.remove_lines_start_with([73, 0])
    expected = 21
    assert actual == expected
