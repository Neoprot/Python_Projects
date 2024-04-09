from sqlalchemy import create_engine, MetaData, Table, ForeignKey
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///:memory')

metadata_obj = MetaData()
user = Table(
    'user',
    metadata_obj,
    Column('user_id', Integer, primary_key=True),
    Column('name', String(40), nullable=False),
    Column('email_address', String(60)),
    Column('nickname', String(50), nullable=False),
)

user_prefs = Table(
    'user_prefs',metadata_obj,
    Column('pref_id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('user.user_id'),nullable=False),
    Column('pref_name', String(40), nullable=False),
    Column('pref_value', String(100)),
)

print("\n Infos of user_prefs Table")
print(user_prefs.primary_key)
print(user_prefs.constraints)

for table in metadata_obj.sorted_tables:
    print(table)

metadata_obj.create_all(engine)

metadata_db_obj = MetaData()
financial_info = Table(
    'financial_info',metadata_db_obj,
    Column('id', Integer, primary_key=True),
    Column('value', String(100), nullable=False),
)

print("\n Infos of financial_info Table")
print(financial_info.primary_key)
print(financial_info.constraints)
