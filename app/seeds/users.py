from app.models import db, User, Server
from datetime import datetime


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password', created_at=datetime.now(), updated_at=datetime.now())
    marnie = User(
        username='marnie', email='marnie@aa.io', password='password', created_at=datetime.now(), updated_at=datetime.now())
    bobbie = User(
        username='bobbie', email='bobbie@aa.io', password='password', created_at=datetime.now(), updated_at=datetime.now())

    db.session.add(demo)
    db.session.add(marnie)
    db.session.add(bobbie)
    # db.session.commit()

    # Add in servers here so that the server objects
    # will have access to user objects
    reg_server_1 = Server(
        name='test-server-1',
        image_url='https://logos-world.net/wp-content/uploads/2020/12/Discord-Logo.png',
        is_dm=False,
        owner_id=1,
        created_at=datetime.now(),
        updated_at=datetime.now())

    reg_server_2 = Server(
        name='test-server-2',
        image_url='https://sm.mashable.com/mashable_sea/photo/default/alexander-shatov-sifcjhruwpm-unsplash_vvnu.jpg',
        is_dm=False,
        owner_id=2,
        created_at=datetime.now(),
        updated_at=datetime.now())

    reg_server_3 = Server(
        name='test-server-3',
        image_url='https://m.media-amazon.com/images/I/51lpm9SpsJL.png',
        is_dm=False,
        owner_id=3,
        created_at=datetime.now(),
        updated_at=datetime.now())

    reg_server_4 = Server(
        name='test-server-4',
        # image_url='',
        is_dm=False,
        owner_id=1,
        created_at=datetime.now(),
        updated_at=datetime.now())

    # Server id 5
    dm_server_1 = Server(
        name='Demo-marnie',
        is_dm=True,
        created_at=datetime.now(),
        updated_at=datetime.now())

    # Server id 6
    dm_server_2 = Server(
        name='Demo-bobbie',
        is_dm=True,
        created_at=datetime.now(),
        updated_at=datetime.now())

    # Server id 7
    dm_server_3 = Server(
        name='marnie-bobbie',
        is_dm=True,
        created_at=datetime.now(),
        updated_at=datetime.now())

    reg_server_1.server_users.append(demo)
    reg_server_1.server_users.append(marnie)
    reg_server_1.server_users.append(bobbie)

    dm_server_1.server_users.append(demo)
    dm_server_1.server_users.append(marnie)

    dm_server_2.server_users.append(demo)
    dm_server_2.server_users.append(bobbie)

    dm_server_3.server_users.append(marnie)
    dm_server_3.server_users.append(bobbie)

    db.session.add(reg_server_1)
    db.session.add(reg_server_2)
    db.session.add(reg_server_3)
    db.session.add(reg_server_4)
    db.session.add(dm_server_1)
    db.session.add(dm_server_2)
    db.session.add(dm_server_3)

    db.session.commit()

# seed_users()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE servers RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
