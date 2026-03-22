from bfrehb import graph_in_box

def test_graph_in_box():
    # Test that the function runs without errors and produces a plot
    try:
        graph_in_box(10)
    except Exception as e:
        assert False, f"graph_in_box raised an exception: {e}"