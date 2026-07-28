from src.statistics import summary

def test_statistics():

    result = summary([
        {
            "todos": [{}, {}]
        }
    ])

    assert result["tasks"] == 2
