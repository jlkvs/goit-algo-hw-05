from typing import List, Tuple, Optional

def binary_search(arr: List[float], target: float) -> Tuple[int, Optional[float]]:
    left, right = 0, len(arr) - 1
    iterations = 0
    upper_bound = None

    while left <= right:
        mid = (left + right) // 2
        iterations += 1

        # Якщо знайдений елемент дорівнює цілі
        if arr[mid] == target:
            return iterations, arr[mid]
        
        # Якщо ціль менше поточного елементу, рухаємо верхню межу
        elif arr[mid] > target:
            upper_bound = arr[mid]
            right = mid - 1
        else:
            left = mid + 1

    return iterations, upper_bound

arr = [1.2, 2.3, 3.4, 4.5, 5.6, 6.7]
target = 4.0
result = binary_search(arr, target)
print(result)  
