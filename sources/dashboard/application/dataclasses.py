from dataclasses import dataclass
from datetime import date


@dataclass
class DayOrdersInfo:
    report_date: date
    total_orders: int
    total_lines: int
    total_cost: float


@dataclass
class PeriodOrdersInfo:
    start_date: date
    end_date: date
    total_orders: int
    total_lines: int
    total_cost: float
