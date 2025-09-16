
# Parallel Computing Mini Project

## Project Title
Parallelize Operations like Map, Reduce, and Scan on Custom Data Structures

## Problem Statement
Large datasets require efficient processing. Sequential execution is slow, 
so we integrate parallel programming techniques with custom data structures.

## Features
- Parallel Map (apply function to all elements)
- Parallel Reduce (aggregate results)
- Parallel Scan (prefix sum)
- Custom `ParallelArray` class

## Applications
- Finance (portfolio aggregation)
- Image Processing (pixel transformation)
- Big Data Analytics (running totals)
- AI/ML Preprocessing (feature transformation)

## Run Instructions
```bash
pip install -r requirements.txt
python examples.py
```

## Dependencies
- Python 3.x
- `concurrent.futures` (built-in)
- `matplotlib` (for visualization)
