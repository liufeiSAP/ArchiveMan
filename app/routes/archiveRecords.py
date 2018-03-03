from flask import Blueprint, render_template, redirect,request
from app import db
from app.dao.archiveRecordDao import ArchiveRecordDao
from app.models.models import ArchiveRecord
archiveRecords = Blueprint('archiveRecords',__name__)

@archiveRecords.route('/index')
def index():
    return render_template('user/index.html')

@archiveRecords.route('/add/',methods=['POST'])
def add():
    p_referdate = request.form.get('referdate',None)
    p_archiveNum = request.form.get('archiveNum',None)
    p_owner = request.form.get('owner',None)
    p_user = request.form.get('user', None)
    p_status = request.form.get('status', None)
    p_returndate = request.form.get('returndate', None)

    # if not p_user or not p_email or not p_password or not p_type:
    #     return 'input error'
    # 增加
    newobj = ArchiveRecord(referdate = p_referdate, archiveNum = p_archiveNum, owner = p_owner, user = p_user, status = p_status, returndate = p_returndate)
    archiveRecordDao = ArchiveRecordDao()
    archiveRecordDao.add(newobj)

@archiveRecords.route('/delete/<archNUMs>', methods=['GET'])
def delete(archNUMs):
    archiveRecordDao = ArchiveRecordDao()
    archiveRecordDao.delete(archNUMs.split(','))

@archiveRecords.route('/update/',methods=['POST'])
def update():
    p_referdate = request.form.get('referdate', None)
    p_archiveNum = request.form.get('archiveNum', None)
    p_owner = request.form.get('owner', None)
    p_user = request.form.get('user', None)
    p_status = request.form.get('status', None)
    p_returndate = request.form.get('returndate', None)

    # if not p_user or not p_email or not p_password or not p_type:
    #     return 'input error'
    # 增加
    newobj = ArchiveRecord(referdate=p_referdate, archiveNum=p_archiveNum, owner=p_owner, user=p_user, status=p_status,
                           returndate=p_returndate)
    archiveRecordDao = ArchiveRecordDao()
    archiveRecordDao.update(newobj)

@archiveRecords.route('/search', methods=['POST'])
def search( ):
    p_start_referdate = request.form.get('start_referdate', None)
    p_end_referdate = request.form.get('end_referdate', None)
    p_archiveNum = request.form.get('archiveNum', None)
    p_owner = request.form.get('owner', None)
    p_user = request.form.get('user', None)
    p_status = request.form.get('status', None)
    p_start_returndate = request.form.get('start_returndate', None)
    p_end_returndate = request.form.get('end_returndate', None)
    archiveRecordDao = ArchiveRecordDao()
    archiveRecordDao.search(p_start_referdate, p_end_referdate, p_archiveNum, p_owner, p_user, p_status, p_start_returndate, p_end_returndate)