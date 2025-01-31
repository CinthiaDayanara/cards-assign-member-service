# 🚀 Microservice `cards-assign-member-service`

## 📌 Description
This microservice allows **assigning members to cards** in a task management system using **GraphQL with FastAPI and PostgreSQL (AWS RDS)**.
It follows the **DRY principle** for reusable assignment logic.

## 🛠️ Technologies
- Python
- FastAPI
- GraphQL (Graphene)
- PostgreSQL (AWS RDS)
- SQLAlchemy (ORM)
- Docker

## 📂 Project Structure
```
cards-assign-member-service/
│── src/
│   ├── graphql/
│   │   ├── resolvers.py
│   │   ├── type_defs.py
│   ├── models/
│   │   ├── database.py
│   │   ├── card.py
│   │   ├── member.py
│   ├── services/
│   │   ├── assignment_service.py ✅ (Reusable logic for assignments)
│   ├── utils/
│   │   ├── validators.py ✅ (Reusable validation functions)
│   ├── app.py
│── server.py
│── Dockerfile
│── docker-compose.yml
│── .env
│── README.md
```

## 🔧 Installation
```sh
pip install -r requirements.txt
```

## 🚀 Running the Microservice
```sh
python server.py
```
Or using Docker:
```sh
docker-compose up --build
```

## 🔗 GraphQL Endpoints
### **1️⃣ Assign a Member to a Card**
```graphql
mutation {
  assignMember(cardId: 1, userId: 2) {
    success
    message
  }
}
```

### **2️⃣ Get Members Assigned to a Card**
```graphql
query {
  getCardMembers(cardId: 1) {
    userId
  }
}
```

## 📄 License
This project is licensed under the MIT License.

