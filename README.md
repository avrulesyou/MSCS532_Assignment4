# Interactive Priority Queue for Task Scheduling

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

1. Run from your terminal:
   ```bash
   python assignment4_p2.py
   ```
2. Interact with the scheduler using the on-screen menu.

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
