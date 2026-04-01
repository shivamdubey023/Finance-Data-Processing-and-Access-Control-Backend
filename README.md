# Finance-Data-Processing-and-Access-Control-Backend (Django + GraphQL)


## 🎯 Objective

Build a backend system for managing financial records with proper role-based access control and analytics support.

The system focuses on:

- Clean backend architecture  
- Role-based permissions  
- Scalable data design  
- GraphQL API implementation  

---

# 🧠 Core Concepts

## 1. Users & Roles

Each user in the system has a defined role that controls their permissions.

### Roles:

| Role    | Permissions                             |
|---------|-----------------------------------------|
| Viewer  | Can only view data                      |
| Analyst | Can view + analyze + update own records |
| Admin   | Full access (CRUD + user management)    |

---

## 2. Data Models

### 👤 User

- username  
- password  
- role (admin / analyst / viewer)  
- is_active  

---

### 📂 Category

- name  

---

### 💰 FinancialRecord

- amount  
- type (income / expense)  
- category (FK → Category)  
- date  
- notes  
- created_by (FK → User)  
- owner (FK → User)  

---

## 🔗 Relationships

- One User → Many Financial Records  
- One Category → Many Financial Records  
- FinancialRecord belongs to:
  - creator (`created_by`)  
  - owner (`assigned user`)  

---

# 🔄 System Flow

## Request Flow:

1. User sends request (GraphQL)  
2. Backend identifies user  
3. Backend checks role  
4. Permission validation happens  
5. Business logic executes  
6. Response returned  

---

# 🛡️ Access Control Logic

## Viewer

- ✅ Can: Read data  
- ❌ Cannot: Create / Update / Delete  

---

## Analyst

- ✅ Can:
  - View records  
  - View analytics  
  - Update OWN records  
- ❌ Cannot:
  - Delete records  
  - Modify others' records  

---

## Admin

- ✅ Can:
  - Create / Read / Update / Delete records  
  - Manage users  
  - Access all data  

---

# ⚙️ API Layer (GraphQL)

## Queries (Read Operations)

- Get all records  
- Get filtered records  
- Get analytics:
  - Total income  
  - Total expense  
  - Net balance  
  - Category breakdown  

---

## Mutations (Write Operations)

- Create record  
- Update record  
- Delete record  
- (Optional) Create user  

---

# 🧠 Business Logic Rules

- Every record must have:
  - creator  
  - owner  
- Only authorized roles can modify data  
- Data must be validated before saving  
- Analytics must be computed from records  

---

# 📊 Example Use Cases

### 1. Admin creates record for analyst

- `created_by = Admin`  
- `owner = Analyst`  

---

### 2. Analyst updates record

- Allowed only if:
  - `record.owner == analyst`  

---

### 3. Viewer tries to delete record

- ❌ Blocked at backend  

---

# 🧱 Project Structure
```
backend/
│
├── users/
├── finance/
│ ├── models.py
│ ├── services.py
│ ├── schema.py
│ ├── permissions.py
│
├── core/
│ └── schema.py
```


---

# 🚀 Key Backend Principles

- Separation of concerns  
- Role-based access control  
- Clean data modeling  
- Secure backend validation  
- Scalable architecture  

---

# 🎯 End Goal

Build a backend that:

- Is logically structured  
- Enforces permissions correctly  
- Handles real-world data scenarios  
- Can power a production-level dashboard  


