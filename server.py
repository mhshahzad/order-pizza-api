"""
Main module of the server file
"""
# local modules
import config

# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")

if __name__ == "__main__":
    connex_app.run(port=5000, debug=False)
