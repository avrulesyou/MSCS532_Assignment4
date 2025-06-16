import sys
import time
import random
import matplotlib.pyplot as plt

# It's good practice to increase recursion limit for Quicksort
sys.setrecursionlimit(20000)

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def quicksort(arr):
    def _quicksort(items, low, high):
        if low < high:
            pivot_index = _partition(items, low, high)
            _quicksort(items, low, pivot_index - 1)
            _quicksort(items, pivot_index + 1, high)
    
    def _partition(items, low, high):
        pivot = items[high]
        i = low - 1
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    _quicksort(arr, 0, len(arr) - 1)

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergesort(left_half)
        mergesort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def run_sorting_comparison():
    sizes = [100, 500, 1000, 2500, 5000, 7500]
    distributions = ["random", "sorted", "reverse_sorted"]
    results = {dist: {"sizes": list(sizes), "heapsort": [], "quicksort": [], "mergesort": []} for dist in distributions}

    for dist in distributions:
        print(f"--- Analyzing {dist.replace('_', ' ').title()} Arrays ---")
        for size in sizes:
            if dist == "random":
                arr = [random.randint(0, size) for _ in range(size)]
            elif dist == "sorted":
                arr = list(range(size))
            else: # reverse_sorted
                arr = list(range(size, -1, -1))

            # Time Heapsort
            arr_copy = arr[:]
            start = time.perf_counter()
            heapsort(arr_copy)
            results[dist]["heapsort"].append(time.perf_counter() - start)
            
            # Time Quicksort
            arr_copy = arr[:]
            start = time.perf_counter()
            quicksort(arr_copy)
            results[dist]["quicksort"].append(time.perf_counter() - start)

            # Time Mergesort
            arr_copy = arr[:]
            start = time.perf_counter()
            mergesort(arr_copy)
            results[dist]["mergesort"].append(time.perf_counter() - start)
            
            print(f"Size: {size:<5} | Heapsort: {results[dist]['heapsort'][-1]:.5f}s | Quicksort: {results[dist]['quicksort'][-1]:.5f}s | Mergesort: {results[dist]['mergesort'][-1]:.5f}s")
            
    # Plotting
    fig, axs = plt.subplots(1, 3, figsize=(20, 6))
    fig.suptitle('Sorting Algorithm Performance Comparison', fontsize=16)
    for i, dist in enumerate(distributions):
        ax = axs[i]
        ax.plot(results[dist]['sizes'], results[dist]['heapsort'], 'o-', label='Heapsort', color='red')
        ax.plot(results[dist]['sizes'], results[dist]['quicksort'], 's-', label='Quicksort', color='blue')
        ax.plot(results[dist]['sizes'], results[dist]['mergesort'], '^-', label='Mergesort', color='green')
        ax.set_title(f"Distribution: {dist.replace('_', ' ').title()}")
        ax.set_xlabel("Input Size (n)")
        ax.set_ylabel("Execution Time (seconds)")
        ax.legend()
        ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == '__main__':
    run_sorting_comparison()
