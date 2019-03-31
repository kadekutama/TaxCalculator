from sanic.response import json
from global_objects import app
from controllers.register_all_controllers import register_routes


register_routes(app)


if __name__ == "__main__":
    app.run(
        host=app.config["HOST"],
        port=app.config["PORT"],
        debug=app.config["DEBUG"],
        workers=app.config["WORKERS"]
    )

# python main.py