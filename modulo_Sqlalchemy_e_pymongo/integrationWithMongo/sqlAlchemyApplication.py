import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, select
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy.sql.functions import user, func

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_account'

    # attributes
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete, delete-orphan"
    )

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, fullname={self.fullname})>"


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True,autoincrement=True)
    email_address = Column(String(40), nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'),nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"<Address (id={self.id}, email_adress={self.email_address})>"


print(Address.__tablename__)

# connection with database
engine = create_engine("sqlite://")

# creating the class as tables in db
Base.metadata.create_all(engine)

# inspects the db schemas
inspector_engine = inspect(engine)

print(inspector_engine.has_table("user_account"))
print(inspector_engine.get_table_names())
print(inspector_engine.default_schema_name)

with Session(engine) as session:
    juliana = User(
        name="juliana",
        fullname="Juliana Mascarenhas",
        address=[Address(email_address="julianam@email.com")]
    )

    sandy = User(
        name="sandy",
        fullname="Sandy Cardoso",
        address=[Address(email_address='sandy@email.br'),
                   Address(email_address='sandy@mail.org')]
    )

    patrick = User(name="patrick",fullname="Patrick Souza")

    # Sending to db (data persistence)
    session.add_all([juliana, sandy, patrick])

    session.commit()

stmt = select(User).where(User.name.in_(['juliana', 'patrick']))
print("Recuperando os dados dos usuários a partir de uma condição de filtragem")
for user in session.scalars(stmt):
    print(user)

stmt_address = select(Address).where(Address.user_id.in_([2]))
print("\nRecuperando os e-mails da Sandy")
for address in session.scalars(stmt_address):
    print(address)

stmt_order = select(User).order_by(User.fullname.desc())
print("\nRecuperando dados de maneira ordenada")
for result in session.scalars(stmt_order):
    print(result)

# this stmt can't bring 2 infos from db using the scalars method
stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
print("\n")
for result in session.scalars(stmt_join):
    print(result)

# with fetchall method the stmt can bring the infos from db for print
connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\n Executando statements a partir da connection")
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print("\n Total de instâncias em User")
for result in session.scalars(stmt_count):
    print(result)
