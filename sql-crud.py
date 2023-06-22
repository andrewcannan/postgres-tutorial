from sqlalchemy import (
    create_engine, Column, Integer, String
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# execute instructions from our localhost "chinook" db
db = create_engine("postgresql:///chinook")
base = declarative_base()


# create class based model for the programmer tble
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connectiong to the database directly, we create a session
# create a new instance if sessionmaker, and point it to our db
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass above
session = Session()

# create db using declarative subclass above
base.metadata.create_all(db)


# creating records on our programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="F",
    nationality="British",
    famous_for="First Programmer"
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="M",
    nationality="British",
    famous_for="Modern Computing"
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="F",
    nationality="American",
    famous_for="COBOL language"
)

margret_hamilton = Programmer(
    first_name="Margret",
    last_name="Hamilton",
    gender="F",
    nationality="American",
    famous_for="Apollo 11"
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="M",
    nationality="American",
    famous_for="Microsoft"
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="M",
    nationality="British",
    famous_for="World Wide Web"
)

andrew_cannan = Programmer(
    first_name="Andrew",
    last_name="Cannan",
    gender="M",
    nationality="Welsh",
    famous_for="Not a lot"
)

# add each instance of programmers to our session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(andrew_cannan)

# commit session to database
# session.commit()

# update a single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "Massive Dong"

# commit session to database
# session.commit()

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# deleting a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(
#     first_name=fname, last_name=lname).first()
# # defensive programming
# if programmer is not None:
#     print("Programmer found: ",
#     programmer.first_name + " " + programmer.last_name)
#     confirmation = input("Are you sure you want to delete this record? (y/n): ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
# else:
#     print("Programmer not found")

# delete all records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

# query the database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )