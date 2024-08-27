let todos = [];

function addTodo() {
    const todoInput = document.getElementById('todoInput');
    const todoDescriptionInput = document.getElementById('todoDescriptionInput');
    
    const todoText = todoInput.value.trim();
    const todoDescription = todoDescriptionInput.value.trim();

    if (todoText === '') {
        alert('Please enter a task');
        return;
    }

    // Simpan task dan deskripsi ke dalam array todos
    todos.push({ text: todoText, description: todoDescription });

    todoInput.value = '';
    todoDescriptionInput.value = '';

    renderTodoList();
}

function removeTodo(index) {
    todos.splice(index, 1);
    renderTodoList();
}

function renderTodoList() {
    const todoList = document.getElementById('todoList');
    todoList.innerHTML = '';

    todos.forEach((todo, index) => {
        const li = document.createElement('li');
        li.className = 'cursor-pointer p-2 hover:bg-gray-200 flex justify-between items-center';
        li.innerText = todo.text;

        const removeButton = document.createElement('button');
        removeButton.innerText = 'Remove';
        removeButton.className = 'ml-4 bg-red-600 text-white rounded ';
        removeButton.addEventListener('click', (e) => {
            e.stopPropagation();
            removeTodo(index);
        });
 
        // Ketika item diklik, tampilkan deskripsi pada elemen #todoDescription
        li.addEventListener('click', () => {
            document.getElementById('todoDescription').innerText = todo.description;
        });

        li.appendChild(removeButton);
        todoList.appendChild(li);
    });
}
