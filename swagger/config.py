from flask_restx import Api
from routes.generate import generate_ns
from routes.template import template_ns

def configure_swagger(app):
    """Configure Swagger UI for the Flask app"""
    api = Api(
        app,
        version='1.0',
        title='Fake Data Generator API',
        description='API for generating realistic fake data for testing and development',
        doc='/swagger',
        validate=True
    )
    
    # Add namespaces to the API
    api.add_namespace(generate_ns, path='/generate')
    api.add_namespace(template_ns, path='/template')
    
    return api