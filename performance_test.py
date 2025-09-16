import time
from parallel_array import ParallelArray

def add(x, y):
    return x + y

def test_performance():
    data = list(range(1, 100000))  # 100k numbers instead of 1M
    arr = ParallelArray(data)

    # Sequential sum
    start = time.time()
    seq_sum = sum(data)
    seq_time = time.time() - start

    # Parallel reduce sum
    start = time.time()
    par_sum = arr.parallel_reduce(add)
    par_time = time.time() - start

    print("Sequential Sum:", seq_sum, "Time:", seq_time)
    print("Parallel Sum:", par_sum, "Time:", par_time)

if __name__ == "__main__":
    test_performance()
