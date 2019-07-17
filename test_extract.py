def test_extract():
    # Sample 10 categories from the method.
    result = extracter.extract(list(range(1000)))

    assert len(result) == 10, "The result doesn't contain 10 categories."

    assert type(result[0]) == "<class 'str'>", "The type of the first element is NOT string."

