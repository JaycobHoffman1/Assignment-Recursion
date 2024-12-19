# Task 1: Design the Task Scheduler Function

def schedule_tasks(task_hierarchy):
    # Task 2: Implement Task Scheduling Logic
    task_schedule = []
    priority_nums = []
    priority = 1

    def find_lowest_priority(task_hierarchy):
        for task in task_hierarchy:
            priority_nums.append(task["priority"])
            if task.get("subtasks", False):
                find_lowest_priority(task["subtasks"])
        lowest_priority = max(priority_nums)
        return lowest_priority

    def add_tasks(task_hierarchy):
        for task in task_hierarchy:
            if task["priority"] == priority:
                task_schedule.append(task["name"])
            if task.get("subtasks", False):
                add_tasks(task["subtasks"])

    lowest_priority = find_lowest_priority(task_hierarchy)

    while priority <= lowest_priority:
        add_tasks(task_hierarchy)
        priority += 1

    return task_schedule

task_hierarchy = [
    {
        "id": "001",
        "name": "clean cat litter boxes",
        "subtasks": [
            {
                "id": "011",
                "name": "scoop cat litter boxes",
                "priority": 3
            },
            {
                "id": "012",
                "name": "dispose of dirty litter",
                "priority": 4
            },
            {
                "id": "013",
                "name": "spray air freshener",
                "priority": 2
            }
        ],
        "priority": 1
    },
    {
        "id": "002",
        "name": "vacuum stairs",
        "subtasks": [
            {
                "id": "021",
                "name": "use vacuum on stairs",
                "priority": 7
            },
            {
                "id": "022",
                "name": "empty vacuum bag",
                "priority": 6
            }
        ],
        "priority": 5
    }
]

# Task 3: Test the Task Scheduler Function

task_schedule = schedule_tasks(task_hierarchy)

print(f"My task schedule: {task_schedule}")

# Task 4: Analyze Time and Space Complexity
'''
The "schedule_tasks" algorithm follows a O(n^2) time complexity. As the number of subtasks grows and the hierarchy branches deeper,
the time for the algorithm to arrange all tasks from greatest priority to lowest priority grows exponentially.
While I do not see any potential optimization strategies for the algorithm, I do see ways the "task_hierarchy" data structure
could be improved to create a new algorithm with a reduced time complexity. For instance, instead of creating tasks with subtasks,
one could simply write all the subtasks in a list. While an algorithm with the same functionality as "schedule_tasks" could
follow a O(n) time complexity, the data structure would be less organized.
'''