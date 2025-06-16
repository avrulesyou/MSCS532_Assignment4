import heapq

class Task:
    def __init__(self, task_id, description, priority):
        self.task_id = task_id
        self.description = description
        self.priority = priority

    def __lt__(self, other):
        # heapq is a min-heap, so lower priority number means higher priority
        return self.priority < other.priority
    
    def __repr__(self):
        return f"Task(ID: {self.task_id}, Priority: {self.priority}, Desc: '{self.description}')"

class PriorityQueue:
    def __init__(self):
        self._heap = []
        self._entry_finder = {} # Maps task_id to heap entry for fast lookups
        self.REMOVED = '<removed-task>' # Placeholder for removed tasks

    def insert(self, task):
        if task.task_id in self._entry_finder:
            print(f"Error: Task with ID {task.task_id} already exists.")
            return
        entry = [task.priority, task.task_id, task]
        self._entry_finder[task.task_id] = entry
        heapq.heappush(self._heap, entry)
        print(f"Inserted: {task}")

    def extract_min(self):
        """Finds and removes all tasks with the highest priority (lowest priority number)."""
        if self.is_empty():
            return []
        
        # Pop the first valid task to determine the minimum priority level
        first_task = None
        while self._heap:
            priority, task_id, task = heapq.heappop(self._heap)
            if task is not self.REMOVED:
                first_task = task
                del self._entry_finder[task_id]
                break
        
        if not first_task:
            return []

        min_priority = first_task.priority
        tasks_to_return = [first_task]

        # Keep popping from the heap as long as the next item has the same minimum priority
        while self._heap and self._heap[0][0] == min_priority:
            priority, task_id, task = heapq.heappop(self._heap)
            if task is not self.REMOVED:
                tasks_to_return.append(task)
                del self._entry_finder[task_id]
        
        return tasks_to_return

    def extract_max(self):
        """Finds, removes, and returns all tasks with the lowest priority."""
        if self.is_empty():
            return []

        # First pass: find the maximum priority value among all active tasks
        max_priority = -1
        for entry in self._entry_finder.values():
            task = entry[2]
            if task is not self.REMOVED and task.priority > max_priority:
                max_priority = task.priority
        
        if max_priority == -1:
            return []

        # Second pass: collect all tasks that have this max priority
        lowest_priority_tasks = []
        for task_id, entry in list(self._entry_finder.items()):
            task = entry[2]
            if task is not self.REMOVED and task.priority == max_priority:
                lowest_priority_tasks.append(task)
                # Mark as removed in the heap list itself and delete from finder
                entry[-1] = self.REMOVED 
                del self._entry_finder[task_id]

        return lowest_priority_tasks

    def get_all_tasks(self):
        """Returns a list of all active tasks in the queue."""
        tasks = []
        for entry in self._entry_finder.values():
            task = entry[2]
            if task is not self.REMOVED:
                tasks.append(task)
        return sorted(tasks, key=lambda t: t.priority)

    def decrease_key(self, task_id, new_priority):
        if task_id not in self._entry_finder:
            print(f"Error: Task with ID {task_id} not found.")
            return
        entry = self._entry_finder[task_id]
        # Mark old entry as removed and push new one
        entry[-1] = self.REMOVED
        
        new_task = Task(task_id, f"Updated priority for task {task_id}", new_priority)
        self.insert(new_task)
        print(f"Updated task {task_id} to new priority {new_priority}.")

    def is_empty(self):
        # A more robust check for emptiness
        for entry in self._heap:
            if entry[-1] is not self.REMOVED:
                return False
        return True

def add_example_tasks(pq, current_id_counter):
    """A helper function to append a predefined set of tasks to the existing list."""
    print("\n--- Appending Example Tasks ---")
    tasks_to_add = [
        ("Coding", 1),
        ("Studying", 1),
        ("Gym", 2),
        ("Gaming", 3)
    ]
    next_id = current_id_counter
    for desc, priority in tasks_to_add:
        task = Task(next_id, desc, priority)
        # Use the internal insert method
        entry = [task.priority, task.task_id, task]
        pq._entry_finder[task.task_id] = entry
        heapq.heappush(pq._heap, entry)
        print(f"Inserted: {task}")
        next_id += 1
    
    print("Example tasks have been added.")
    print("----------------------------\n")
    return next_id # Return the next available ID

def interactive_scheduler():
    pq = PriorityQueue()
    task_id_counter = 1

    while True:
        print("\n--- Priority Queue Task Scheduler ---")
        print("1. Add a new task")
        print("2. Get the highest-priority task(s)")
        print("3. Get the lowest-priority task(s)")
        print("4. Update a task's priority")
        print("5. Load example tasks (appends to current list)")
        print("6. Print all pending tasks")
        print("7. Check if queue is empty")
        print("8. Exit")
        
        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            try:
                desc = input("Enter task description: ")
                priority = int(input("Enter priority (lower number is higher priority): "))
                task = Task(task_id_counter, desc, priority)
                pq.insert(task)
                task_id_counter += 1
            except ValueError:
                print("Invalid input. Priority must be an integer.")

        elif choice == '2':
            tasks = pq.extract_min()
            if tasks:
                print(f"\n--- Highest-Priority Task(s) ---")
                for task in tasks:
                    print(task)
                print("----------------------------------")
            else:
                print("The priority queue is empty.")
        
        elif choice == '3':
            tasks = pq.extract_max()
            if tasks:
                print(f"\n--- Lowest-Priority Task(s) ---")
                for task in tasks:
                    print(task)
                print("-----------------------------")
            else:
                print("The priority queue is empty.")

        elif choice == '4':
            try:
                task_id = int(input("Enter the ID of the task to update: "))
                new_priority = int(input("Enter the new, lower priority number: "))
                pq.decrease_key(task_id, new_priority)
            except ValueError:
                print("Invalid input. Please enter integers for ID and priority.")
        
        elif choice == '5':
            task_id_counter = add_example_tasks(pq, task_id_counter)

        elif choice == '6':
            all_tasks = pq.get_all_tasks()
            if not all_tasks:
                print("The task list is empty.")
            else:
                print("\n--- All Current Tasks (sorted by priority) ---")
                print(f"{'ID':<5} | {'Priority':<10} | {'Description'}")
                print("-" * 40)
                for task in all_tasks:
                    print(f"{task.task_id:<5} | {task.priority:<10} | {task.description}")
                print("-" * 40)

        elif choice == '7':
            if pq.is_empty():
                print("The priority queue is empty.")
            else:
                print("The priority queue is not empty.")

        elif choice == '8':
            print("Exiting scheduler.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == '__main__':
    interactive_scheduler()
