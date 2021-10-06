from classic.http_api import App

from dashboard.application.interfaces import OrdersInfoRepoInterface

from . import controllers


def create_app(orders_info_repo: OrdersInfoRepoInterface) -> App:
    app = App()

    app.register(
        controllers.OrderReports(orders_info_repo=orders_info_repo),
    )

    return app
