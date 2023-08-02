import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class User:
    id: int
    name: str
    email: str

my_db = [{"id": 1, "name": "Abc", "email": "abc@example.com"},{"id": 2, "name": "Pqr", "email": "pqr@example.com"},{"id": 3, "name": "Xyz", "email": "Xyz@example.com"},]

@strawberry.type
class Query:
    @strawberry.field
    def user(self, id:int) -> User:
        for user in my_db:
            if id == user["id"]:
                return User(**user)

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(
    schema,
)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")