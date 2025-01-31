import uvicorn
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from src.graphql.type_defs import schema

app = FastAPI()

# Montar GraphQL en FastAPI
app.add_route("/graphql", GraphQLApp(schema=schema))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5008)
