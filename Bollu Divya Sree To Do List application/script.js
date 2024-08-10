document.addEventListener('DOMContentLoaded', function () {
    const todoForm = document.getElementById('todo-form');
    const todoInput = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');

    // Load existing todos from local storage
    const savedTodos = JSON.parse(localStorage.getItem('todos')) || [];

    // Render todos on page load
    savedTodos.forEach(todo => {
        addTodoToDOM(todo.text, todo.completed);
    });

    todoForm.addEventListener('submit', function (event) {
        event.preventDefault();
        const newTodoText = todoInput.value.trim();

        if (newTodoText !== '') {
            addTodoToDOM(newTodoText);
            saveTodoToLocalStorage(newTodoText);
            todoInput.value = '';
        }
    });

    function addTodoToDOM(text, completed = false) {
        const todoItem = document.createElement('li');
        todoItem.classList.add('todo-item');
        if (completed) {
            todoItem.classList.add('completed');
        }
        todoItem.textContent = text;

        const deleteBtn = document.createElement('button');
        deleteBtn.textContent = 'Delete';
        deleteBtn.classList.add('delete-btn');

        deleteBtn.addEventListener('click', function () {
            todoItem.remove();
            removeTodoFromLocalStorage(text);
        });

        todoItem.addEventListener('click', function () {
            todoItem.classList.toggle('completed');
            toggleTodoInLocalStorage(text);
        });

        todoItem.appendChild(deleteBtn);
        todoList.appendChild(todoItem);
    }

    function saveTodoToLocalStorage(todoText) {
        const todos = JSON.parse(localStorage.getItem('todos')) || [];
        todos.push({ text: todoText, completed: false });
        localStorage.setItem('todos', JSON.stringify(todos));
    }

    function removeTodoFromLocalStorage(todoText) {
        let todos = JSON.parse(localStorage.getItem('todos')) || [];
        todos = todos.filter(todo => todo.text !== todoText);
        localStorage.setItem('todos', JSON.stringify(todos));
    }

    function toggleTodoInLocalStorage(todoText) {
        const todos = JSON.parse(localStorage.getItem('todos')) || [];
        const todo = todos.find(todo => todo.text === todoText);
        if (todo) {
            todo.completed = !todo.completed;
        }
        localStorage.setItem('todos', JSON.stringify(todos));
    }
});
