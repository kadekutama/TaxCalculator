from sanic.response import html, HTTPResponse
from typing import Optional
from global_objects import jinja_env


def render_template(template_name: str, status_code: Optional[int] = 200, headers: Optional[dict] = None, **kwargs) -> HTTPResponse:
    template_file = jinja_env.get_template(template_name)
    return html(template_file.render(kwargs), status=status_code, headers=headers)