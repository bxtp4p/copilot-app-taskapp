from flask import Blueprint, render_template, redirect, url_for, request
from extensions import db
from models import Task
from forms import TaskForm
from services import TaskService

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/')
def get_tasks():
    """
    Fetch all tasks and display them on the task list page.

    Returns:
    - A rendered template for the task list page with all tasks.
    """
    tasks = TaskService.get_all_tasks()
    return render_template('task_list.html', tasks=tasks)

@task_blueprint.route('/add', methods=['GET', 'POST'])
def add_task():
    """
    Add a new task based on form submission. If the form is not submitted,
    display the form for adding a new task.

    Returns:
    - A redirect to the task list page if the form is successfully submitted.
    - A rendered template for adding a new task if the form is not submitted.
    """
    form = TaskForm()
    if form.validate_on_submit():
        TaskService.add_task(
            form.title.data,
            form.description.data,
            form.done.data
        )
        return redirect(url_for('tasks.get_tasks'))
    
    return render_template('add_task.html', form=form)

@task_blueprint.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    """
    Edit an existing task based on form submission. If the form is not submitted,
    display the form pre-filled with the task's current details.

    Parameters:
    - task_id: The ID of the task to be edited.

    Returns:
    - A redirect to the task list page if the form is successfully submitted.
    - A rendered template for editing the task if the form is not submitted.
    """
    task = TaskService.get_task_by_id(task_id)
    form = TaskForm(obj=task)
    
    if form.validate_on_submit():
        TaskService.update_task(
            task,
            form.title.data,
            form.description.data,
            form.done.data
        )
        return redirect(url_for('tasks.get_tasks'))
    
    return render_template('edit_task.html', form=form)

@task_blueprint.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    """
    Delete a task based on its ID.

    Parameters:
    - task_id: The ID of the task to be deleted.

    Returns:
    - A redirect to the task list page after the task is deleted.
    """
    TaskService.delete_task(TaskService.get_task_by_id(task_id))
    return redirect(url_for('tasks.get_tasks'))

if __name__ == '__main__':
    app.run(debug=True)
