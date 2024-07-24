from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Initialize an empty todo list
todo_list = []
next_id = 1  # Initialize ID counter


@app.route('/')
def index():
    return render_template('index.html', tasks=todo_list)


@app.route('/add_task', methods=['POST'])
def add_task():
    global next_id
    task_content = request.form['content']
    deadline = request.form['deadline'] if 'deadline' in request.form else None
    new_task = {'id': next_id, 'task': task_content, 'completed': False, 'important': False, 'deadline': deadline}
    todo_list.append(new_task)
    next_id += 1
    return redirect(url_for('index'))


@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    for task in todo_list:
        if task['id'] == task_id:
            task['completed'] = True
            break
    return redirect(url_for('index'))


@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    global todo_list
    todo_list = [task for task in todo_list if task['id'] != task_id]
    return redirect(url_for('index'))


@app.route('/mark_important/<int:task_id>')
def mark_important(task_id):
    for task in todo_list:
        if task['id'] == task_id:
            task['important'] = True
            break
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
