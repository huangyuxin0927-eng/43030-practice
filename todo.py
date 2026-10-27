class Task:
    # Constructor initializes the task with title and status
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.completed = False
        self.status = status

    # Marks the task as completed and changes its status to "Done"
    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    # Returns a string representation of the task
    def __repr__(self):
        return f"{self.title} - {'Done' if self.completed else 'ToDo'}"

    # Returns a human-readable string representation of the task
    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        task1 = Task("Task 1")
        task2 = Task("Task 2")
        task3 = Task("Task 3")
        task4 = Task("Task 4")
        task5 = Task("Task 5")
        task6 = Task("Task 6")

        task1.mark_completed()
        task2.mark_completed()
        task3.mark_completed()

        self.tasks = [task1, task2, task3, task4, task5, task6]

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [task for task in self.tasks if task.status == "ToDo"]

    def get_done_tasks(self):
        return [task for task in self.tasks if task.status == "Done"]


def main():
    pool = TaskPool()
    pool.populate()

    open_tasks = pool.get_open_tasks()
    done_tasks = pool.get_done_tasks()

    print("ToDo Tasks:")
    for task in open_tasks:
        print(task.title)

    print("Done Tasks:")
    for task in done_tasks:
        print(task.title)


if __name__ == "__main__":
    main()
