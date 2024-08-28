from extensions import db

class Task(db.Model):
    """
    Task model for representing a task in the database.

    Attributes:
    - id (int): Unique identifier for the task.
    - title (str): Title of the task, cannot be null.
    - description (str): Detailed description of the task, can be null.
    - done (bool): Status of the task, defaults to False (not done).
    """

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        """
        Provide a string representation of the Task instance.

        Returns:
        - A string representation of the Task instance.
        """
        return f'<Task {self.title}>'