from sqlalchemy import TIMESTAMP, Column, Integer, MetaData, String, Table

metadata = MetaData()

opeartion = Table(
    "opeartion",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("quantity", String),
    Column("figi", String),
    Column("instrument_type", String, nullable=True),
    Column("date", TIMESTAMP),
    Column("type", String),
)
