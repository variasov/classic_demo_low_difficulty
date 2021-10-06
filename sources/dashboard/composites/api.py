from sqlalchemy import create_engine

from classic.aspects import points
from classic.sql_storage import TransactionContext

from dashboard.adapters.database import repositories, metadata, DBSettings
from dashboard.adapters.api import create_app


# Secondary adapters

# Database
db_settings = DBSettings()
engine = create_engine(db_settings.DB_URL)
metadata.create_all(engine)

transaction_ctx = TransactionContext(bind=engine)

orders_info_repo = repositories.OrdersInfoRepo(context=transaction_ctx)

points.join(transaction_ctx)


# Primary adapters

# API
app = create_app(orders_info_repo)
