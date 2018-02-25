from app import db #db是在app/__init__.py生成的关联后的SQLAlchemy实例
from app.userType import UserType
from app.archStatus import ArchStatus
import enum

race_enums = ('asian','mideastern','black')
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)    # 用户名
    email = db.Column(db.String(320), unique=True)      # 邮箱
    password = db.Column(db.String(32), nullable=False) # 密码
    type = db.Column(db.Integer , nullable=False)       # 一般用户/ 领导 / 管理员
    #gender = db.Column(enum.Enum('M', 'F'), nullable=False)  # ENUM cause compiler error , why ???

    def __repr__(self):
        return '<User %r>' % self.username

class ArchiveRecord(db.Model):
    __tablename__ = 'ArchiveRecord'
    id = db.Column(db.Integer, primary_key=True)
    referdate = db.Column(db.Date, nullable = False)    #  调档日期
    archiveNum = db.Column(db.String(80), unique=True)  #  公证书号
    owner = db.Column(db.String(80), unique=False)      #  当事人
    user = db.Column(db.String(80), nullable=False)     #  用卷人
    status = db.Column(db.String(80), nullable=False)      #  当前状态
    returndate =  db.Column(db.Date, nullable = False)  #  归还日期

    def update(self, other):
        self.referdate = other.referdate
        self.archiveNum = other.archiveNum
        self.owner = other.owner
        self.user = other.user
        self.status = other.status
        self.referdate = other.referdate

    def __repr__(self):
        return '<ArchiveNum %r>' % self.archiveNum

class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
