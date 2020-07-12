import flask

from pypi_org.services import user_service, package_service, cms_service
from pypi_org.viewmodels.shared.viewmodelbase import ViewModelBase


class RequestViewModel(ViewModelBase):
    def __init__(self, url):
        super().__init__()
        self.url = url

    @property
    def page(self):
        page = cms_service.get_page(base_url=self.url)
        return page

    @property
    def redirect(self):
        redirect = cms_service.get_redirect(base_url=self.url)
        return redirect

    @property
    def redirect_urL(self):
        dest = None
        if self.redirect:
            dest = self.redirect.get('url')
        query_string = flask.request.query_string
        if query_string:
            dest = f'{dest}?{query_string.decode("utf-8")}'
        return dest
