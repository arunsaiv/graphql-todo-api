# 📝 GraphQL Todo API (Python + FastAPI + Strawberry + SQLite)

A minimal and modern **GraphQL API for a Todo app**, built with:

- 🐍 Python
- ⚡ FastAPI
- 🍓 Strawberry (GraphQL)
- 💾 SQLite + SQLModel
- 🐳 Docker-ready
- 🌐 Deployed via Render

Explore how to build a practical GraphQL API with type-safety, queries, mutations, filtering, and persistence.

---

## 🚀 Features

- Add, complete, and delete todos
- Filter by completed status
- GraphQL Playground UI (`/graphql`)
- REST-free API structure
- Fully Dockerized & deployable

---

## 🛠 Tech Stack

| Layer        | Tech                  |
|--------------|------------------------|
| Language     | Python 3.11            |
| Web Framework| FastAPI                |
| GraphQL      | Strawberry             |
| ORM / DB     | SQLModel + SQLite      |
| Container    | Docker                 |
| Deploy       | Render                 |

---

## 📦 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/arunsaiv/graphql-todo-api.git
cd graphql-todo-api
```
### Install Dependencies

```bash
pip install -r requirements.txt
```

### 3.Run Locally

```bash
uvicorn main:app --reload
```

---

## 🐳 Run with Docker

### 1. Build Image

```bash
docker build -t graphql-todo .
```

### 2. Run Container

```bash
docker run -d -p 8000:8000 graphql-todo
```

---

## 🔧 Example GraphQL Queries

### Add a Todo

```bash
mutation {
  addTodo(title: "Write blog") {
    id
    title
    completed
  }
}
```

### Get All Todos

```bash
query {
  allTodos {
    id
    title
    completed
  }
}
```

### Mark Todo Completed

```bash
mutation {
  markCompleted(id: 1) {
    id
    completed
  }
}
```

### Delete a Todo

```bash
mutation {
  deleteTodo(id: 1)
}
```

---

### 🌐 Live Demo

🔗 https://graphql-todo-api.onrender.com/graphql

---

🧱 Coming Soon
-	✅ React + Apollo Client UI
-	🌐 Frontend deployment with Netlify/Vercel

---

📄 License

MIT License

---

👨‍💻 Author

Made with ❤️ by Arun Sai Veerisetty 

If you found this helpful:

- ⭐ Star the repo
- 📢 Share with others
- 🧠 Contribute ideas or patterns
