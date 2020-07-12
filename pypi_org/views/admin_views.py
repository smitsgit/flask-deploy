import flask

from pypi_org.infrastructure import permissions
from pypi_org.infrastructure.view_modifiers import response
from pypi_org.services import cms_service
from pypi_org.viewmodels.admin.redirect_viewmodel import RedirectListViewModel
from pypi_org.viewmodels.cms.request_viewmodel import RequestViewModel
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase

blueprint = flask.Blueprint('admin', __name__, template_folder='templates')


@blueprint.route('/admin')
@response(template_file='admin/index.html')
@permissions.admin
def index():
    vm = ViewModelBase()
    return vm.to_dict()


@blueprint.route('/admin/redirects')
@response(template_file='admin/redirects.html')
@permissions.admin
def redirects():
    vm = RedirectListViewModel()
    return vm.to_dict()
