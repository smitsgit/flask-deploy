import flask

from pypi_org.services import user_service, package_service, cms_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class RedirectListViewModel(ViewModelBase):
    def __init__(self):
        super().__init__()
        self.redirects = cms_service.get_all_redirects()
