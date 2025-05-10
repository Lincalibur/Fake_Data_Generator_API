
**Prompt:**

You are a senior backend developer and full-stack engineer. I want to build a Flask-based **Fake Data Generator API** that can be used by developers and QA teams to generate realistic test data. The app should support both:

1. A **Swagger/OpenAPI documentation page** at `/swagger`
2. A **simple web UI** for manual use (e.g., select type of data, count, copy result)

---

### 📦 **Tech Stack:**

* **Backend:** Python Flask
* **API Docs:** Swagger (via Flask-RESTX or Flask-Swagger-UI)
* **UI:** Simple HTML/CSS + JavaScript (rendered via Jinja2 or separate `/ui` route)
* **Data Generator:** Use `Faker` library for names, emails, etc.
* **Deployment:** Ready to run as a Flask app locally or behind Docker

---

### 🧩 **Core Endpoints:**

#### 1. `GET /generate`

Generate a list of fake data for a given type.

**Query Parameters:**

* `type` = one of `name`, `email`, `address`, `lorem`, `phone`, `company`, etc.
* `count` = number of entries (default 1)

**Example:**

```
GET /generate?type=email&count=10
```

**Returns:**

```json
{
  "type": "email",
  "count": 10,
  "data": [
    "john.doe@example.com",
    "alice@domain.net",
    ...
  ]
}
```

---

#### 2. `POST /template`

Accepts a JSON body with a mock schema, returns generated mock JSON.

**Example Input:**

```json
{
  "template": {
    "userId": "uuid4",
    "email": "email",
    "isActive": "boolean",
    "registeredAt": "date_time"
  },
  "count": 3
}
```

**Returns:**

```json
[
  {
    "userId": "7e799e29-37a1-4032-b75d-0dc4d632f232",
    "email": "fakeuser@mail.com",
    "isActive": true,
    "registeredAt": "2024-05-07T14:32:12"
  },
  ...
]
```

---

### 🌐 **Web UI (`/ui`):**

* Accessible in browser
* Two panels:

  * **Simple Generator**: Choose type (dropdown) + count → shows result
  * **Template Generator**: Paste schema, enter count → shows result
* Copy-to-clipboard and JSON beautifier

---

### ✅ **Requirements:**

* Flask app with modular structure (`routes`, `utils`, `schemas`)
* Integrated Swagger UI at `/swagger`
* Optional rate limiting to prevent abuse
* CORS-enabled for frontend use
* Easily deployable via Docker

---

### 📁 **Folder Structure:**

```
fake-data-api/
│
├── app.py
├── routes/
│   ├── generate.py
│   └── template.py
├── utils/
│   └── data_generator.py
├── templates/
│   └── ui.html
├── static/
│   └── style.css
├── requirements.txt
└── swagger/
    └── config.py (Flask-RESTX or Flask-Swagger-UI)
```

---

**Request:**
Please generate:

* Flask app scaffolding with Swagger setup at `/swagger`
* `/generate` and `/template` endpoints using `Faker`
* A simple UI at `/ui` for manual data generation
* Sample `requirements.txt`

