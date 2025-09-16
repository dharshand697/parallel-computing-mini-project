from concurrent.futures import ProcessPoolExecutor
import itertools

class ParallelArray:
    def __init__(self, data):
        self.data = data

    def parallel_map(self, func, workers=4):
        """Apply a function to each element in parallel."""
        with ProcessPoolExecutor(max_workers=workers) as executor:
            result = list(executor.map(func, self.data))
        return ParallelArray(result)

    def parallel_reduce(self, func):
        """Reduce elements pairwise in parallel (fixed to handle odd lengths)."""
        with ProcessPoolExecutor() as executor:
            data = self.data
            while len(data) > 1:
                it = iter(data)
                reduced = list(executor.map(func, it, it))
                # If odd length, keep last element
                if len(data) % 2 == 1:
                    reduced.append(data[-1])
                data = reduced
            return data[0]

    def parallel_scan(self):
        """Compute prefix sums (currently sequential)."""
        result = list(itertools.accumulate(self.data))
        return ParallelArray(result)
