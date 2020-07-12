import flask
from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import cms_service
from pypi_org.viewmodels.cms.request_viewmodel import RequestViewModel

blueprint = flask.Blueprint('cms', __name__, template_folder='templates')


# @response()
@blueprint.route('/<path:full_url>')
def cms_handler(full_url):
    vm = RequestViewModel(full_url)
    # Check if the full_url matches some page or redirect
    if vm.page:
        return f"Title: {vm.page.get('title')}, Contents: {vm.page.get('contents')}"
    if vm.redirect:
        return flask.redirect(vm.redirect_urL)
    return flask.abort(404)
