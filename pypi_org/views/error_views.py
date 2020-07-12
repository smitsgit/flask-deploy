import flask
from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import cms_service

blueprint = flask.Blueprint('errors', __name__, template_folder='templates')


# @response()
@blueprint.app_errorhandler(404)
def error_404(error):
    resp = flask.render_template("errors/404.html")
    return resp, 404
