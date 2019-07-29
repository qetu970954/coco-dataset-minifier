from utilities.LineRemover import LineRemover
from tests.test_setup import setup_working_directory

def test_LineRemover(setup_working_directory):
    # Remove lines for the directory.
    remover = LineRemover("tests/resources/tmp/")

    actual = remover.remove_lines_start_with([73, 0])
    expected = 18
    assert actual == expected
