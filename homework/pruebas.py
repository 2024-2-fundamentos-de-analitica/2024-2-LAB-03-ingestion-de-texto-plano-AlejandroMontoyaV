from homework import pregunta_01 as pregunta

def test_01():
    """Test homework"""

    df = pregunta.pregunta_01()

    # Test 1
    assert df.cluster.to_list() == list(range(1, 14))

test_01()