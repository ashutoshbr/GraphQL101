```graphql
# query
{
  user(id:3){
    id
    email
  }
}


# response
{
  "data": {
    "user": {
      "id": 3,
      "email": "Xyz@example.com"
    }
  }
}
```