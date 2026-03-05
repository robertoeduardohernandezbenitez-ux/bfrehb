from bfrehb import knapsap_problem

def test_knapsap():
    weigth=[2,3,4]
    profits=[3,4,5]
    capacity=5
    goal=7
    assert knapsap_problem(weigth,profits,capacity,goal)==(1, 1, 0)

    weigth=[2,3,4]
    profits=[3,4,5]
    capacity=5
    goal=8
    assert knapsap_problem(weigth,profits,capacity,goal)==False