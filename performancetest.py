import datetime
from recursive import recursive_floyd_warshall
from imperative import floydwarshall

INF = 9999
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]


def compare_functions():
    start_time = datetime.datetime.now()
    for i in range(0, 10000):
        recursive_floyd_warshall(graph)
    end_time = datetime.datetime.now()
    time1 = end_time - start_time
    print("Time taken by Recursive Version:")
    print(time1)

    start_time = datetime.datetime.now()
    for i in range(0, 10000):
        floydwarshall(graph)
    end_time = datetime.datetime.now()
    time2 = end_time - start_time
    print("Time taken by Imperative Version:")
    print(time2)

if __name__ == "__main__":
    compare_functions()