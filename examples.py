from parallel_array import ParallelArray

# Define functions at top-level (not lambdas)
def square(x):
    return x * x

def add(x, y):
    return x + y

if __name__ == "__main__":
    # Example: Basic Operations
    arr = ParallelArray([13, 240, 43, 44, 45])

    print("Original Data:", arr.data)
    print("Parallel Map (square):", arr.parallel_map(square).data)
    print("Parallel Reduce (sum):", arr.parallel_reduce(add))
    print("Parallel Scan (prefix sum):", arr.parallel_scan().data)

    # Example: Real-time Application - Portfolio Value (Finance)
    prices = ParallelArray([1040, 2040, 30440, 4040, 5400])
    portfolio_value = prices.parallel_reduce(add)
    print("Portfolio Total Value:", portfolio_value)



