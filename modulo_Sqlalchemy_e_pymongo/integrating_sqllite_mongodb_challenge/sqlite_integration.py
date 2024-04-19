import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, select, Float
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()

class Clients(Base):
    __tablename__ = 'clients'

    # Creating the attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    cpf = Column(String, nullable=False)
    address = Column(String)

    account = relationship('Account', back_populates='clients', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, fullname={self.cpf})>"

class Account(Base):
    __tablename__ = 'account'

    # Creating attributes
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String)
    agency = Column(String, nullable=False)
    number = Column(Integer, nullable=False, unique=True)
    id_cliente = Column(Integer, ForeignKey('clients.id'), nullable=False)
    balance = Column(Float)

    clients = relationship('Clients', back_populates='account')

    def __repr__(self):
        return f"<User(id={self.id}, type={self.type}, agency={self.agency}, number={self.number}, balance={self.balance})>"


# making the connection with database
engine = create_engine("sqlite://")

# creating the class as tables in db
Base.metadata.create_all(engine)

# inspects the db schemas
inspector_engine = inspect(engine)

print(inspector_engine.has_table("clients"))
print(inspector_engine.get_table_names())
print(inspector_engine.default_schema_name)



with Session(engine) as session:
    juliana = Clients(
        name="juliana",
        cpf="123.456.789-01",
        address="Augusta",
        account=[Account(type="Conta corrente",agency="0001",number=1,balance=190.5)]
    )

    sandy = Clients(
        name="sandy",
        cpf="123.456.789-02",
        address="São Paulo",
        account=[Account(type="Conta Poupança",agency="0001",number=2,balance=60.2)]
    )

    patrick = Clients(name="patrick",cpf="123.456.789-06",address="Lisboa")

    # Sending to db (data persistence)
    session.add_all([juliana, sandy, patrick])

    session.commit()


stmt = select(Clients).where(Clients.name.in_(['juliana', 'patrick']))
print("Recuperando os dados dos usuários a partir de uma condição de filtragem")
for client in session.scalars(stmt):
    print(client)

stmt_account = select(Account).where(Account.id_cliente.in_([2]))
print("\nRecuperando os e-mails da Sandy")
for account in session.scalars(stmt_account):
    print(account)
