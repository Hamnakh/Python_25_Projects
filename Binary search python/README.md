# Binary Search Implementation in Python

This project implements the binary search algorithm in Python, providing both iterative and recursive approaches. Binary search is a fundamental divide-and-conquer algorithm that efficiently searches for an element in a sorted array.

## Features

- Iterative binary search implementation
- Recursive binary search implementation
- Time complexity: O(log n)
- Space complexity: O(1) for iterative, O(log n) for recursive
- Example usage with test cases

## How Binary Search Works

Binary search works by repeatedly dividing the search interval in half. It compares the middle element with the target value and eliminates half of the remaining elements in each step. This makes it much more efficient than linear search for large datasets.

### Algorithm Steps:
1. Find the middle element of the array
2. Compare the middle element with the target value
3. If they match, return the index
4. If the middle element is greater than the target, search in the left half
5. If the middle element is less than the target, search in the right half
6. Repeat until the element is found or the search space is empty

## Usage

```python
# Example array (must be sorted)
arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

# Using iterative binary search
result = binary_search_iterative(arr, target)

# Using recursive binary search
result = binary_search_recursive(arr, target, 0, len(arr) - 1)
```

## Requirements

- Python 3.x

## Running the Code

1. Clone this repository or download the files
2. Navigate to the project directory
3. Run the program:
```bash
python app.py
```

## Time and Space Complexity

- **Time Complexity**: O(log n)
  - The search space is halved in each step
  - For an array of size n, it takes log₂(n) steps to find the element

- **Space Complexity**:
  - Iterative: O(1) - uses only a constant amount of extra space
  - Recursive: O(log n) - due to the recursion stack

## Important Notes

1. The input array must be sorted
2. Returns -1 if the element is not found
3. Works efficiently on large datasets
4. Not suitable for unsorted arrays

## Example Output

```
Element 7 found at index 3 (Iterative)
Element 7 found at index 3 (Recursive)
```

## Contributing

Feel free to submit issues and enhancement requests! 