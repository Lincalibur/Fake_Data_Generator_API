from flask import Blueprint, request, jsonify
from flask_restx import Resource, Namespace
from utils.data_generator import generate_fake_data

generate_bp = Blueprint('generate', __name__)
generate_ns = Namespace('generate', description='Generate fake data based on type')

@generate_ns.route('')
class GenerateData(Resource):
    @generate_ns.doc(params={
        'type': {'description': 'Type of data to generate', 'enum': [
            'name', 'email', 'address', 'phone', 'company', 'text', 'date', 
            'credit_card', 'job', 'color', 'url', 'ipv4', 'ipv6', 'user_agent'
        ]},
        'count': {'description': 'Number of items to generate', 'default': 1}
    })
    def get(self):
        """Generate a list of fake data for a given type"""
        data_type = request.args.get('type', 'name')
        count = int(request.args.get('count', 1))
        
        # Limit count to prevent abuse
        if count > 100:
            count = 100
            
        data = generate_fake_data(data_type, count)
        
        return jsonify({
            'type': data_type,
            'count': count,
            'data': data
        })

# Route for non-Swagger access
@generate_bp.route('/generate', methods=['GET'])
def generate_data():
    data_type = request.args.get('type', 'name')
    count = int(request.args.get('count', 1))
    
    # Limit count to prevent abuse
    if count > 100:
        count = 100
        
    data = generate_fake_data(data_type, count)
    
    return jsonify({
        'type': data_type,
        'count': count,
        'data': data
    })