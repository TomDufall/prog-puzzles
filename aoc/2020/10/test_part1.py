from part1 import count_diffs, join_adaptors, validate_adaptor_chain

def test_e2e():
    adaptors = [16,10,15,5,1,11,7,19,6,12,4]
    expected = {
        1: 7,
        3: 5,
    }
    assert count_diffs(join_adaptors(adaptors)) == expected