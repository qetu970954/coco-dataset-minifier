from utilities.CategoryRearranger import CategoryRearranger


def test_CategoryRearranger(setup_working_directory):
    rearranger = CategoryRearranger([58, 62, 0], "tests/resources/tmp/")

    actual = rearranger.foundation
    expected = {58: 0, 62: 1, 0: 2}
    assert type(actual) == type(expected), "The type of the foundation is incorrect."
    assert actual == expected, "The foundation (1-to-1 mapping) does not look correct."

    actual = rearranger.rearrange()
    expected = 7
    assert actual == expected
