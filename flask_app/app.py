from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# initialize an empty list to store our to-do items
todo_items = []

@app.route('/')
def index():
    """Render the index page with the list of to-do items."""
    return render_template('index.html', todo_items=todo_items)

@app.route('/add', methods=['POST'])
def add():
    """Add a new to-do item to the list."""
    item = request.form['item']
    todo_items.append(item)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    """Delete a to-do item from the list."""
    del todo_items[index]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
