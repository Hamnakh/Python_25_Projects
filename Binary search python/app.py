def binary_search_iterative(arr, target):
    """Iterative implementation of binary search"""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(arr, target, left, right):
    """Recursive implementation of binary search"""
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def run_test_case(arr, target):
    print(f"\nSearching for {target} in array: {arr}")

    result_iterative = binary_search_iterative(arr, target)
    if result_iterative != -1:
        print(f"✅ Found {target} at index {result_iterative} (Iterative)")
    else:
        print(f"❌ {target} not found (Iterative)")

    result_recursive = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if result_recursive != -1:
        print(f"✅ Found {target} at index {result_recursive} (Recursive)")
    else:
        print(f"❌ {target} not found (Recursive)")


def main():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]

    # Test Case 1: Number exists
    print("📌 Test Case 1: Element Exists")
    run_test_case(arr, 7)

    # Test Case 2: Number does not exist
    print("\n📌 Test Case 2: Element Does Not Exist")
    run_test_case(arr, 6)


if __name__ == "__main__":
    main()
