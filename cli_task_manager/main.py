# main.py

import click
from cli_task_manager.database import create_connection, create_tables, insert_task, get_all_tasks
from cli_task_manager.task import Task

@click.group()
def cli():
    pass

@cli.command()
@click.option('--title', prompt='Task title', help='Title of the task')
@click.option('--description', prompt='Description', help='Description of the task')
@click.option('--priority', type=click.Choice(['high', 'medium', 'low']), prompt='Priority', help='Task priority')
@click.option('--due-date', prompt='Due date', help='Due date of the task')
@click.option('--status', type=click.Choice(['incomplete', 'complete']), default='incomplete', prompt='Status', help='Task status')
def add_task(title, description, priority, due_date, status):
    """Add a new task."""
    conn = create_connection()
    create_tables(conn)
    task_data = (title, description, priority, due_date, status)
    insert_task(conn, task_data)
    click.echo('Task added successfully.')

@cli.command()
def list_tasks():
    """List all tasks."""
    conn = create_connection()
    tasks = get_all_tasks(conn)
    for task_data in tasks:
        task = Task(*task_data[1:])
        click.echo(task)
        click.echo('-' * 30)

@cli.command()
@click.argument('task_id', type=int)
def update_status(task_id):
    """Update the status of a task."""
    conn = create_connection()
    create_tables(conn)
    new_status = click.prompt('New status (incomplete/complete)', type=click.Choice(['incomplete', 'complete']))
    if update_task_status(conn, task_id, new_status):
        click.echo(f'Task {task_id} updated successfully.')
    else:
        click.echo(f'Task {task_id} not found.')

@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Delete a task."""
    conn = create_connection()
    create_tables(conn)
    

    if delete_task(conn, task_id):
        click.echo(f'Task {task_id} deleted successfully.')
    else:
        click.echo(f'Task {task_id} not found.')


if __name__ == '__main__':
    cli()
