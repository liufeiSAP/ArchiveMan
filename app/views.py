from app import app
from app.routes.login import login
from app.routes.archiveRecords import archiveRecords
from app.routes.admin import admin
from app.routes.user import user


app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(archiveRecords, url_prefix='/archiveRecords')
app.register_blueprint(login, url_prefix='/login')

