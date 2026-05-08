
import pytest
from todo_app.models import Task

def test_task_init():
    task = Task('Finish project', 'High')
    assert task.title == 'Finish project'
    assert task.priority == 'High'

@pytest.mark.parametrize("title, priority", [
    ('Finish project', 'High'),
    ('Buy milk', 'Low'),
])
def test_task_string_representation(title, priority):
    task = Task(title, priority)
    assert str(task) == f"Task: {title} (Priority: {priority})"

def test_task_priority_range():
    with pytest.raises(ValueError):
        _ = Task('Finish project', 'Invalid Priority')
