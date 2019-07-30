from utilities.Extractor import Extractor


def test_extract():
    extractor = Extractor("tests/resources/coco.names")
    extracted_item, remains = extractor.extract(30)

    assert len(extracted_item) == 30, "The result doesn't contain expected number of categories."
    assert len(remains) == 50, "Remain doesn't contain expected number of categories."
    assert str(type(extracted_item)) == "<class 'dict'>", "The type of the first element is NOT string."

    for key in extracted_item.keys():
        assert type(key) is int, "The type of each keys should be an integer."

    for val in extracted_item.values():
        assert type(val) is str, "The type of each values should be a string"


def test_extract_specific():
    extractor = Extractor("tests/resources/coco.names")
    extracted_items, remains = extractor.extract_specific(
        ['truck', 'tie', 'sheep', 'dog', 'airplane',
         'bus', 'suitcase', 'toothbrush', 'sink', 'bench']
    )

    assert len(extracted_items) == 10, "The result doesn't contain expected number of categories."
    assert len(remains) == 70, "Remain doesn't contain expected number of categories."
    assert str(type(extracted_items)) == "<class 'dict'>", "The type of the first element is NOT string."

    for key in extracted_items.keys():
        assert type(key) is int, "The type of each keys should be an integer."

    for val in extracted_items.values():
        assert type(val) is str, "The type of each values should be a string"

    assert extracted_items == {4 : 'airplane', 5: 'bus', 7: 'truck', 13: 'bench', 16: 'dog', 18: 'sheep', 27: 'tie',
                              28: 'suitcase', 71: 'sink', 79: 'toothbrush'}
