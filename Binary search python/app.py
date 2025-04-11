def binary_search_iterative(arr, target):
    """
    Iterative implementation of binary search
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Element not found

def binary_search_recursive(arr, target, left, right):
    """
    Recursive implementation of binary search
    Time Complexity: O(log n)
    Space Complexity: O(log n) due to recursion stack
    """
    if left > right:
        return -1  # Element not found
    
    mid = (left + right) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

def main():
    # Example array
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    
    # Test Case 1: Number that exists in array
    print("Test Case 1: Searching for 7 (exists in array)")
    target = 7
    
    # Test iterative binary search
    result_iterative = binary_search_iterative(arr, target)
    if result_iterative != -1:
        print(f"Element {target} found at index {result_iterative} (Iterative)")
    else:
        print(f"Element {target} not found (Iterative)")
    
    # Test recursive binary search
    result_recursive = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if result_recursive != -1:
        print(f"Element {target} found at index {result_recursive} (Recursive)")
    else:
        print(f"Element {target} not found (Recursive)")
    
    # Test Case 2: Number that doesn't exist in array
    print("\nTest Case 2: Searching for 6 (doesn't exist in array)")
    target = 6
    
    # Test iterative binary search
    result_iterative = binary_search_iterative(arr, target)
    if result_iterative != -1:
        print(f"Element {target} found at index {result_iterative} (Iterative)")
    else:
        print(f"Element {target} not found (Iterative)")
    
    # Test recursive binary search
    result_recursive = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if result_recursive != -1:
        print(f"Element {target} found at index {result_recursive} (Recursive)")
    else:
        print(f"Element {target} not found (Recursive)")

if __name__ == "__main__":
    main()
