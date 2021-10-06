from datetime import date

from classic.components import component
from classic.sql_storage import BaseRepository
from sqlalchemy import select, func, distinct
from pydantic import validate_arguments

from dashboard.application.interfaces import OrdersInfoRepoInterface
from dashboard.application.dataclasses import DayOrdersInfo, PeriodOrdersInfo

from .tables import orders, order_lines


@component
class OrdersInfoRepo(BaseRepository, OrdersInfoRepoInterface):

    @validate_arguments
    def get_for_day(self, day: date) -> DayOrdersInfo:
        query = select(
            func.count(distinct(orders.c.number)).label('orders_number'),
            func.count(orders.c.number).label('lines_number'),
            func.sum(
                order_lines.c.quantity * order_lines.c.price
            ).label('orders_cost'),
        ).select_from(
            orders.join(order_lines)
        ).where(
            func.date(orders.c.order_date) == day
        )

        result = self.session.execute(query).one_or_none()
        return DayOrdersInfo(
            day,
            result.orders_number,
            result.lines_number,
            result.orders_cost or 0,
        )

    @validate_arguments
    def get_for_period(self, start_day: date,
                       end_day: date) -> PeriodOrdersInfo:
        query = select(
            func.count(distinct(orders.c.number)).label('orders_number'),
            func.count(orders.c.number).label('lines_number'),
            func.sum(
                order_lines.c.quantity * order_lines.c.price
            ).label('orders_cost'),
        ).select_from(
            orders.join(order_lines)
        ).where(
            func.DATE(orders.c.order_date) >= start_day,
            func.DATE(orders.c.order_date) < end_day,
        )

        result = self.session.execute(query).one_or_none()
        return PeriodOrdersInfo(
            start_day, end_day,
            result.orders_number,
            result.lines_number,
            result.orders_cost or 0
        )
