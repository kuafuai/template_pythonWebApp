# Import necessary modules and libraries
from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Define API routes and their corresponding functions
@app.route('/')
def home():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run()
