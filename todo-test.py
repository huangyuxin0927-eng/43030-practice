import unittest
from todo import Task, TaskPool


class TestTaskPool(unittest.TestCase):

    def setUp(self):
        self.task_pool = TaskPool()

    def test_add_task(self):
        task = Task("New Task")
        self.task_pool.add_task(task)

        self.assertEqual(len(self.task_pool.tasks), 1)
        self.assertEqual(self.task_pool.tasks[0].title, "New Task")

    def test_get_open_tasks(self):
        self.task_pool.populate()

        open_tasks = self.task_pool.get_open_tasks()

        self.assertEqual(len(open_tasks), 3)
        for task in open_tasks:
            self.assertEqual(task.status, "ToDo")

    def test_get_done_tasks(self):
        self.task_pool.populate()

        done_tasks = self.task_pool.get_done_tasks()

        self.assertEqual(len(done_tasks), 3)
        for task in done_tasks:
            self.assertEqual(task.status, "Done")


if __name__ == "__main__":
    unittest.main(verbosity=2)
