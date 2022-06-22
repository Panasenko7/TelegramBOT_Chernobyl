employees = {}
from models import User, engine

from sqlalchemy.orm import Session


def add_employee(name):
    with Session(engine) as session:
        user = User(name=name, working_hours=0)
        session.add_all([user])
        session.commit()
        print(f'We added user {name}')


def remove_employee(name):
    with Session(engine) as session:
        # user = User(name=name, working_hours=0)
        user = session.query(User).filter_by(name=name).first()
        if user is None:
            print('No such user')
            return

        session.delete(user)
        session.commit()
        print(f'We removed user {name}')

        return True


def get_employees():
    list_with_employees = []

    with Session(engine) as session:
        for element in session.query(User).all():
            list_with_employees.append(str(element))
        return list_with_employees
