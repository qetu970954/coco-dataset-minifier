from utilities.Extractor import Extractor


def test_extract():
    extractor = Extractor()
    extractor.read_from("tests/resources/coco.names")
    extracted_item, remain = extractor.extract(10)

    assert len(extracted_item) == 10, "The result doesn't contain 10 categories."
    assert len(remain) == 70
    assert str(type(extracted_item)) == "<class 'dict'>", "The type of the first element is NOT string."

    for key in extracted_item.keys():
        assert type(key) is int, "The type of each keys should be integer."

    for val in extracted_item.values():
        assert type(val) is str, "The type of each values should be string"
