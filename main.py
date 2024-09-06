while True:
	# Get user input and strip space chars from it
	user_action = input("Type add, show, edit, complete, or exit: ")
	user_action = user_action.strip()

	if 'add' in user_action:
		todo = user_action[4:] + '\n'

		with open('files/todos.txt', 'r') as file:
			todos = file.readlines()

		todos.append(todo)

		with open('files/todos.txt', 'w') as file:
			todos = file.writelines(todos)

	if 'show' in user_action:
		with open('files/todos.txt', 'r') as file:
			todos = file.readlines()

		for index, item in enumerate(todos):
			item = item.strip('\n')
			row = f"{index + 1}-{item}"
			print(row)

	if 'edit' in user_action:
		number = int(input("Number of the todo to edit: "))
		number = number - 1

		with open('files/todos.txt', 'r') as file:
			todos = file.readlines()

		new_todo = input("Enter new todo: ")
		todos[number] = new_todo + '\n'

		with open('files/todos.txt', 'w') as file:
			todos = file.writelines(todos)

	if 'complete' in user_action:
		number = int(input("Number of the todo to complete: "))

		with open('files/todos.txt', 'r') as file:
			todos = file.readlines()
		index = number - 1
		todo_to_remove = todos[index].strip('\n')
		todos.pop(index)

		with open('files/todos.txt', 'w') as file:
			todos = file.writelines(todos)

		message = f"Todo {todo_to_remove} was removed from the list."
		print(message)

	if 'exit' in user_action:
		break

print("Bye!")

