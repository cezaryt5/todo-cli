# 📝 Todo CLI

A modern, user-friendly command-line todo application built with Python. Manage your tasks efficiently with a beautiful terminal interface.

## ✨ Features

- **Add Tasks** - Quickly add new tasks to your list
- **List Tasks** - View all tasks in a beautiful table format or JSON
- **Complete Tasks** - Mark tasks as completed with timestamps
- **Edit Tasks** - Update task descriptions
- **Delete Tasks** - Remove tasks with confirmation
- **Persistent Storage** - Tasks are saved locally in JSON format
- **Rich Terminal UI** - Beautiful tables and colored output

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd todo-cli
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## 📖 Usage

### Run the application

```bash
# Using Python module
python -m todo_cli

# Or directly
python todo_cli/cli.py
```

### Commands

#### Add a new task
```bash
python -m todo_cli add "Buy groceries"
```

#### List all tasks
```bash
# Display in table format (default)
python -m todo_cli list

# Show all tasks including completed
python -m todo_cli list --all

# Output as JSON
python -m todo_cli list --format json
```

#### Mark a task as completed
```bash
python -m todo_cli complete 1
```

#### Edit a task
```bash
python -m todo_cli edit 1 "Buy groceries and cook dinner"
```

#### Delete a task
```bash
# With confirmation
python -m todo_cli delete 1

# Skip confirmation
python -m todo_cli delete 1 --force
```

#### Show task details
```bash
python -m todo_cli show 1
```

#### Show version
```bash
python -m todo_cli --version
```

## 🏗️ Project Structure

```
todo-cli/
├── todo_cli/           # Main package
│   ├── __init__.py     # Package initialization
│   ├── __main__.py     # Entry point for module execution
│   ├── cli.py          # CLI interface and commands
│   ├── core/           # Core application logic
│   │   ├── __init__.py
│   │   └── todo.py     # TodoApp class with business logic
│   ├── commands/       # Command implementations
│   │   └── __init__.py
│   └── utils/          # Utility functions
│       └── __init__.py
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore patterns
└── README.md          # This file
```

## 🛠️ Technologies Used

- **Python 3.8+** - Core programming language
- **Typer** - Modern CLI framework for building command-line interfaces
- **Rich** - Library for rich text and beautiful formatting in the terminal

## 💡 Key Design Decisions

1. **Modular Architecture**: Separated concerns into core logic, CLI interface, and utilities
2. **Type Hints**: Full type annotation for better code clarity and IDE support
3. **JSON Storage**: Simple, human-readable persistent storage
4. **User Experience**: Colorful output, emojis, and intuitive command names
5. **Error Handling**: Graceful handling of missing files and invalid inputs

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Created as a demonstration of Python CLI development skills.

---

*Built with ❤️ using Python, Typer, and Rich*
