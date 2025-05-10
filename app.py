from flask import Flask, render_template
from flask_cors import CORS
from routes.generate import generate_bp
from routes.template import template_bp
from swagger.config import configure_swagger

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Register blueprints
app.register_blueprint(generate_bp)
app.register_blueprint(template_bp)

# Configure Swagger
api = configure_swagger(app)

@app.route('/ui')
def ui():
    """Render the UI for manual data generation"""
    return render_template('ui.html')

@app.route('/')
def index():
    """Redirect to Swagger UI"""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)