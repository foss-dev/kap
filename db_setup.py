# To Do

# Buraya ilk kurulum için ayarları gerçekleştirmeye yardım edecek bazı configler gelecek.
# Daha önceden kurulum yapılmışsa bunu çalıştırmak yerine yeni bir çözüm üretilebilir.

from werkzeug import generate_password_hash

from tracer.data.models import db, User, Role
from tracer import app

db.init_app(app)

def create_roles(ctx):
    role = Role('admin')

    ctx.session.add(role)
    ctx.session.commit()


def create_user(ctx):
    email = 'admin@admin'
    name = 'John Doe'
    password = generate_password_hash('admin')
    is_active = True
    roles = 1
    user = User(
        email=email, name=name, password=password, active=is_active, roles=roles)
    
    ctx.session.add(user)

    ctx.session.commit()


with app.app_context():
    db.drop_all()
    db.create_all()

    create_roles(db)
    create_user(db)