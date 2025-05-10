from flask import Blueprint, request, jsonify
from flask_restx import Resource, Namespace, fields
from utils.data_generator import generate_from_template

template_bp = Blueprint('template', __name__)
template_ns = Namespace('template', description='Generate fake data based on a template')

# Define the template model for Swagger documentation
template_model = template_ns.model('Template', {
    'template': fields.Raw(description='Template schema with field names and types', required=True),
    'count': fields.Integer(description='Number of items to generate', default=1)
})

template_example = {
    'template': {
        'userId': 'uuid4',
        'email': 'email',
        'isActive': 'boolean',
        'registeredAt': 'date_time'
    },
    'count': 3
}

@template_ns.route('')
class TemplateData(Resource):
    @template_ns.doc(body=template_model)
    @template_ns.doc(params={'example': {'description': 'Example template', 'default': template_example}})
    def post(self):
        """Generate fake data based on a template schema"""
        data = request.get_json()
        
        if not data or 'template' not in data:
            return jsonify({'error': 'Template is required'}), 400
            
        template = data.get('template', {})
        count = int(data.get('count', 1))
        
        # Limit count to prevent abuse
        if count > 100:
            count = 100
            
        result = generate_from_template(template, count)
        
        return jsonify(result)

# Route for non-Swagger access
@template_bp.route('/template', methods=['POST'])
def template_data():
    data = request.get_json()
    
    if not data or 'template' not in data:
        return jsonify({'error': 'Template is required'}), 400
        
    template = data.get('template', {})
    count = int(data.get('count', 1))
    
    # Limit count to prevent abuse
    if count > 100:
        count = 100
        
    result = generate_from_template(template, count)
    
    return jsonify(result)