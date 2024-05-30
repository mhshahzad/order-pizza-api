"""
Main module of the server file
"""
# local modules
import config
import os

# Get the application instance
connex_app = config.connex_app

# # Read the swagger.yml file to configure the endpoints
connex_app.add_api("openapi-3.0.yml")


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    connex_app.run(host='127.0.0.1', port=port, debug=False)
