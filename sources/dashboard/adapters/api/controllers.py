from classic.aspects import join_point
from classic.components import component

from dashboard.application.interfaces import OrdersInfoRepoInterface


@component
class OrderReports:
    orders_info_repo: OrdersInfoRepoInterface

    @join_point
    def on_get_report_for_day(self, request, response):
        info = self.orders_info_repo.get_for_day(**request.params)
        response.media = {
            'date': info.report_date.isoformat(),
            'orders': info.total_orders,
            'lines': info.total_lines,
            'cost': info.total_cost,
        }

    @join_point
    def on_get_report_for_period(self, request, response):
        info = self.orders_info_repo.get_for_period(**request.params)
        response.media = {
            'start': info.start_date.isoformat(),
            'end': info.end_date.isoformat(),
            'orders': info.total_orders,
            'lines': info.total_lines,
            'cost': info.total_cost,
        }
