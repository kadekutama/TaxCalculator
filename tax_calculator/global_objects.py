from sanic import Sanic
from jinja2 import Environment, FileSystemLoader, select_autoescape
from os.path import dirname, realpath
from sys import path as sys_path
from gino.ext.sanic import Gino
import asyncio
from config import CONFIG


project_dir = dirname(realpath(__file__))
sys_path.append(project_dir)
app = Sanic(name=CONFIG["APP_NAME"])
app.config.update(CONFIG)
if not CONFIG["DEBUG"]:
    app.config.ACCESS_LOG = False
db = Gino()
db.init_app(app)
jinja_env = Environment(loader=FileSystemLoader(f"{project_dir}/views"), autoescape=select_autoescape(["html"]))