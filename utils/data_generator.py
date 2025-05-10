from faker import Faker
import uuid
import random
import datetime

fake = Faker()

# Map of supported data types and their corresponding Faker methods
DATA_TYPES = {
    'name': fake.name,
    'email': fake.email,
    'address': fake.address,
    'phone': fake.phone_number,
    'company': fake.company,
    'text': fake.paragraph,
    'date': lambda: fake.date_time().strftime('%Y-%m-%d'),
    'date_time': lambda: fake.date_time().strftime('%Y-%m-%dT%H:%M:%S'),
    'credit_card': fake.credit_card_number,
    'job': fake.job,
    'color': fake.color_name,
    'url': fake.url,
    'ipv4': fake.ipv4,
    'ipv6': fake.ipv6,
    'user_agent': fake.user_agent,
    'uuid4': lambda: str(uuid.uuid4()),
    'boolean': lambda: random.choice([True, False]),
    'integer': lambda: random.randint(1, 1000),
    'float': lambda: round(random.uniform(1.0, 1000.0), 2)
}

def generate_fake_data(data_type, count=1):
    """Generate fake data of a specific type"""
    if data_type not in DATA_TYPES:
        return [f"Unsupported data type: {data_type}"] * count
    
    return [DATA_TYPES[data_type]() for _ in range(count)]

def generate_from_template(template, count=1):
    """Generate fake data based on a template schema"""
    result = []
    
    for _ in range(count):
        item = {}
        for field, field_type in template.items():
            if field_type in DATA_TYPES:
                item[field] = DATA_TYPES[field_type]()
            else:
                item[field] = f"Unsupported field type: {field_type}"
        result.append(item)
    
    return result