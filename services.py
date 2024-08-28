from models import Task
from extensions import db

class TaskService:
    @staticmethod
    def get_all_tasks():
        """
        Fetch all tasks from the database.

        Returns:
        - A list of all Task instances.
        """
        return Task.query.all()

    @staticmethod
    def get_task_by_id(task_id):
        """
        Fetch a single task by its ID.

        Parameters:
        - task_id: The ID of the task to fetch.

        Returns:
        - A Task instance corresponding to the given ID, or None if not found.
        """
        return Task.query.get(task_id)

    @staticmethod
    def add_task(title, description, done):
        """
        Add a new task to the database.

        Parameters:
        - title: The title of the task.
        - description: The description of the task.
        - done: Boolean indicating whether the task is done.

        Returns:
        - The newly created Task instance.
        """
        new_task = Task(
                title=title,
                description=description,
                done=done
        )
        db.session.add(new_task)
        db.session.commit()
        return new_task
    
    @staticmethod
    def update_task(task, title, description, done):
        """
        Update an existing task.

        Parameters:
        - task: The Task instance to update.
        - title: The new title for the task.
        - description: The new description for the task.
        - done: Boolean indicating the new done status.

        Returns:
        - The updated Task instance.
        """
        task.title = title
        task.description = description
        task.done = done
        db.session.commit()
        return task

    @staticmethod
    def delete_task(task):
        """
        Delete a task from the database.

        Parameters:
        - task: The Task instance to delete.

        Returns:
        - The deleted Task instance.
        """
        db.session.delete(task)
        db.session.commit()
        return task