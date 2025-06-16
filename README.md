# Assignment 4: Sorting and Priority Queue Implementation

This repository contains two distinct projects:
1. **Heapsort Implementation and Analysis**: A comparative study of sorting algorithms
2. **Interactive Priority Queue**: A task scheduler using binary heap implementation

## 📁 Project Files

| File | Description |
|------|-------------|
| `assignment4_p1.py` | Main script for Heapsort implementation and analysis |
| `assignment4_p2.py` | Priority Queue implementation using binary heap |
| `requirements.txt` | Python package dependencies |
| `assignment4_p1.pdf` | Analysis Document for Part 1 (Heapsort) |
| `assignment4_p2.pdf` | Analysis Document for Part 2 (Priority Queue) |
| `assignment4.png` | Visualization of sorting algorithm performance |
| `Readme.md` | Project documentation |

---

# Project 1: Heapsort Implementation and Analysis

This project provides an implementation of the Heapsort algorithm and empirically compares its performance against Quicksort and Mergesort.

The goal is to analyze the efficiency of these algorithms across different input sizes and data distributions (random, sorted, and reverse-sorted) and to visualize the results.

## 📂 Key Features

- **Heapsort Implementation**: A clear and efficient implementation of the Heapsort algorithm using an array to represent the heap.
- **Comparative Analysis**: The script runs all three sorting algorithms on identical datasets to provide a fair performance comparison.
- **Data Visualization**: Automatically generates plots to visually represent the running times of the algorithms, making it easy to understand their performance characteristics.
- **Multiple Data Distributions**: Tests algorithms on random, sorted, and reverse-sorted arrays to highlight best-case, average-case, and worst-case scenarios.

## 🚀 How to Run

Set up the environment:

```bash
# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

Run the analysis script:

```bash
python assignment4_p1.py
```

The script will print the timing results to the console and then display a series of plots comparing the algorithms' performance.

## 📋 Example Performance Results

Below is the sample output from running the analysis script.

### Random Arrays
```
Size: 100   | Heapsort: 0.00026s | Quicksort: 0.00015s | Mergesort: 0.00023s
Size: 500   | Heapsort: 0.00176s | Quicksort: 0.00084s | Mergesort: 0.00174s
Size: 1000  | Heapsort: 0.00640s | Quicksort: 0.00218s | Mergesort: 0.00298s
Size: 2500  | Heapsort: 0.01459s | Quicksort: 0.00565s | Mergesort: 0.00927s
Size: 5000  | Heapsort: 0.03389s | Quicksort: 0.01811s | Mergesort: 0.02017s
Size: 7500  | Heapsort: 0.04549s | Quicksort: 0.01862s | Mergesort: 0.03260s
```

### Sorted Arrays
```
Size: 100   | Heapsort: 0.00026s | Quicksort: 0.00092s | Mergesort: 0.00020s
Size: 500   | Heapsort: 0.00195s | Quicksort: 0.02019s | Mergesort: 0.00111s
Size: 1000  | Heapsort: 0.00647s | Quicksort: 0.08136s | Mergesort: 0.00249s
Size: 2500  | Heapsort: 0.01275s | Quicksort: 0.32479s | Mergesort: 0.00416s
Size: 5000  | Heapsort: 0.01642s | Quicksort: 1.40167s | Mergesort: 0.01747s
Size: 7500  | Heapsort: 0.05194s | Quicksort: 3.02286s | Mergesort: 0.02548s
```

### Reverse Sorted Arrays
```
Size: 100   | Heapsort: 0.00015s | Quicksort: 0.00039s | Mergesort: 0.00012s
Size: 500   | Heapsort: 0.00096s | Quicksort: 0.01323s | Mergesort: 0.00335s
Size: 1000  | Heapsort: 0.00253s | Quicksort: 0.04896s | Mergesort: 0.00151s
Size: 2500  | Heapsort: 0.00876s | Quicksort: 0.34985s | Mergesort: 0.00823s
Size: 5000  | Heapsort: 0.02781s | Quicksort: 1.16925s | Mergesort: 0.01790s
Size: 7500  | Heapsort: 0.04251s | Quicksort: 2.29813s | Mergesort: 0.01499s
```

---

# Project 2: Interactive Priority Queue for Task Scheduling

This project is an interactive command-line application that implements a Priority Queue using a binary heap. It's designed to simulate a simple task scheduler where tasks are processed based on their assigned priority.

The implementation uses a min-heap, meaning tasks with a lower priority number are considered higher priority.

## 📂 Key Features

- **Dynamic Task Management**: Add new tasks with a description and priority. Task IDs are assigned automatically.
- **Priority-Based Extraction**: Retrieve and remove the highest-priority task(s) or the lowest-priority task(s). The implementation correctly handles multiple tasks that share the same priority level.
- **Priority Updates**: Modify the priority of an existing task using its ID.
- **Lazy Deletion**: Uses a placeholder system (`<removed-task>`) for efficient key updates and deletions without needing to rebuild the entire heap.
- **Example Loader**: Quickly populate the queue with a predefined set of example tasks.
- **Formatted Task List**: View all current tasks in a clean, sorted table.

## 🚀 How to Run

This script is self-contained and does not require any external libraries beyond standard Python.

1. Save the code as a Python file (e.g., `assignment4_part2.py`)
2. Run from your terminal:
   ```bash
   python assignment4_part2.py
   ```
3. Interact with the scheduler using the on-screen menu.

## 📋 Example Usage

Below is a sample session demonstrating the interactive menu and its features.

```
--- Priority Queue Task Scheduler ---
1. Add a new task
2. Get the highest-priority task(s)
3. Get the lowest-priority task(s)
4. Update a task's priority
5. Load example tasks (appends to current list)
6. Print all tasks
7. Check if queue is empty
8. Exit
```

### Sample Session

```
Enter your choice (1-8): 1
Enter task description: Cycling
Enter priority (lower number is higher priority): 3
Inserted: Task(ID: 1, Priority: 3, Desc: 'Cycling')

--- Priority Queue Task Scheduler ---
1. Add a new task
2. Get the highest-priority task(s)
3. Get the lowest-priority task(s)
4. Update a task's priority
5. Load example tasks (appends to current list)
6. Print all tasks
7. Check if queue is empty
8. Exit
Enter your choice (1-8): 6

--- All Current Tasks (sorted by priority) ---
ID    | Priority   | Description
----------------------------------------
1     | 3          | Cycling
----------------------------------------
```

### Task Management Examples

#### Adding Example Tasks
```
--- Appending Example Tasks ---
Inserted: Task(ID: 2, Priority: 1, Desc: 'Coding')
Inserted: Task(ID: 3, Priority: 1, Desc: 'Studying')
Inserted: Task(ID: 4, Priority: 2, Desc: 'Gym')
Inserted: Task(ID: 5, Priority: 3, Desc: 'Gaming')
Example tasks have been added.
```

#### Viewing Tasks
```
--- All Current Tasks (sorted by priority) ---
ID    | Priority   | Description
----------------------------------------
2     | 1          | Coding
3     | 1          | Studying
4     | 2          | Gym
1     | 3          | Cycling
5     | 3          | Gaming
----------------------------------------
```

#### Getting Highest Priority Tasks
```
--- Highest-Priority Task(s) ---
Task(ID: 2, Priority: 1, Desc: 'Coding')
Task(ID: 3, Priority: 1, Desc: 'Studying')
----------------------------------
```

#### Getting Lowest Priority Tasks
```
--- Lowest-Priority Task(s) ---
Task(ID: 1, Priority: 3, Desc: 'Cycling')
Task(ID: 5, Priority: 3, Desc: 'Gaming')
-----------------------------
```

## 📝 Notes

- Tasks with the same priority are processed in the order they were added
- The system uses a min-heap implementation, so lower priority numbers indicate higher priority
- Task IDs are automatically assigned and are unique
- The queue can handle multiple tasks with the same priority level
