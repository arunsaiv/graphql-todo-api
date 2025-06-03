# Import necessary modules
import strawberry
from typing import List, Optional
from model import Todo as DBTodo  # Database model for Todo
from db import get_session        # Function to get DB session
from sqlmodel import select       # Used to build SQL queries

from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from db import create_db_and_tables  # Function to initialize DB and tables

# GraphQL type used for schema responses
@strawberry.type
class Todo:
    id: int
    title: str
    completed: bool

# GraphQL Query class for fetching todos
@strawberry.type
class Query:

    # Fetch all todos, with optional filtering by completion status
    @strawberry.field
    def all_todos(self, completed: Optional[bool] = None) -> List[Todo]:
        with get_session() as session:
            query = select(DBTodo)
            if completed is not None:
                query = query.where(DBTodo.completed == completed)
            results = session.exec(query).all()
            return [Todo(**todo.dict()) for todo in results]

# GraphQL Mutation class for adding, updating, and deleting todos
@strawberry.type
class Mutation:

    # Add a new todo with the given title
    @strawberry.mutation
    def add_todo(self, title: str) -> Todo:
        with get_session() as session:
            todo = DBTodo(title=title)
            session.add(todo)
            session.commit()
            session.refresh(todo)
            return Todo(**todo.dict())

    # Mark a specific todo as completed by ID
    @strawberry.mutation
    def mark_completed(self, id: int) -> Optional[Todo]:
        with get_session() as session:
            todo = session.get(DBTodo, id)
            if todo:
                todo.completed = True
                session.add(todo)
                session.commit()
                session.refresh(todo)
                return Todo(**todo.dict())
            return None

    # Delete a specific todo by ID
    @strawberry.mutation
    def delete_todo(self, id: int) -> bool:
        with get_session() as session:
            todo = session.get(DBTodo, id)
            if todo:
                session.delete(todo)
                session.commit()
                return True
            return False

# Build the GraphQL schema from the Query and Mutation classes
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Create a FastAPI application
app = FastAPI()

# Initialize the database and tables at startup
create_db_and_tables()

# Mount the GraphQL app at the /graphql endpoint
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
