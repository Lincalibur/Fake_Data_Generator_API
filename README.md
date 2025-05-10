# Fake Data Generator API

A Flask-based API for generating realistic fake data for development and testing purposes. This tool helps developers and QA teams quickly generate test data in various formats.

![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🚀 Features

- **RESTful API** with Swagger/OpenAPI documentation
- **Web UI** for easy manual data generation
- **Multiple data types** support (names, emails, addresses, etc.)
- **Template-based generation** for complex data structures
- **Dark/Light mode** for the web interface
- **Docker support** for easy deployment

## 📋 Available Data Types

The API supports generating the following types of fake data:

- `name` - Full names
- `email` - Email addresses
- `address` - Physical addresses
- `phone` - Phone numbers
- `company` - Company names
- `text` - Lorem ipsum paragraphs
- `date` - Dates in YYYY-MM-DD format
- `date_time` - Datetime in ISO format
- `credit_card` - Credit card numbers
- `job` - Job titles
- `color` - Color names
- `url` - Web URLs
- `ipv4` - IPv4 addresses
- `ipv6` - IPv6 addresses
- `user_agent` - Browser user agents
- `uuid4` - UUID version 4 strings
- `boolean` - True/False values
- `integer` - Random integers
- `float` - Random floating-point numbers

## 🛠️ Installation

### Prerequisites

- Python 3.8+
- pip

### Local Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/Fake_Data_Generator_API.git
cd Fake_Data_Generator_API
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
python app.py
```

The API will be available at http://127.0.0.1:5000

### Docker Setup

1. Build and run using Docker Compose:

```bash
docker-compose up -d
```

The API will be available at http://localhost:5000

## 📚 API Usage

### Simple Data Generation

#### GET /generate

Generate a list of fake data for a given type.

**Query Parameters:**

- `type` - Type of data to generate (see available data types above)
- `count` - Number of items to generate (default: 1, max: 100)

**Example Request:**

```
GET /generate?type=email&count=3
```

**Example Response:**

```json
{
  "type": "email",
  "count": 3,
  "data": [
    "john.doe@example.com",
    "alice.smith@domain.net",
    "bob.johnson@test.org"
  ]
}
```

### Template-based Generation

#### POST /template

Generate complex data structures based on a template schema.

**Request Body:**

```json
{
  "template": {
    "userId": "uuid4",
    "email": "email",
    "isActive": "boolean",
    "registeredAt": "date_time"
  },
  "count": 2
}
```

**Example Response:**

```json
{
  "count": 2,
  "data": [
    {
      "userId": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
      "email": "john.doe@example.com",
      "isActive": true,
      "registeredAt": "2023-09-15T14:30:21"
    },
    {
      "userId": "a3e56378-7c9b-4d53-b0f3-4675a92d43e5",
      "email": "alice.smith@domain.net",
      "isActive": false,
      "registeredAt": "2023-08-22T09:15:43"
    }
  ]
}
```

## 🖥️ Web UI

The application includes a user-friendly web interface for generating fake data without writing code.

- **Simple Generator**: Generate basic data types with a specified count
- **Template Generator**: Create complex data structures using a JSON template
- **Dark/Light Mode**: Toggle between dark and light themes

Access the web UI at: http://127.0.0.1:5000/ui

## 📖 Documentation

Interactive API documentation is available via Swagger UI at: http://127.0.0.1:5000/swagger

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.