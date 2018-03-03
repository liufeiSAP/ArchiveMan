from app.models.models import ArchiveRecord
from app import db

class ArchiveRecordDao:
    def add(self, p_archiveRec):
        db.session.add(p_archiveRec)
        db.session.commit()

    def delete(self, p_username):
        users = db.session.query(ArchiveRecord).filter(ArchiveRecord.archiveNum.in_(p_username)).delete(synchronize_session=False)
        db.session.commit()

    def update(self, p_archiveRec):
        rec = db.session.query(ArchiveRecord).filter_by(archiveNum = p_archiveRec.archiveNum).first()
        if not rec:
            self.add(p_archiveRec)
        else:
            rec.update(p_archiveRec)

        db.session.commit()

    def search(self, p_start_referdate, p_end_referdate, p_archiveNum, p_owner, p_user, p_status, p_start_returndate, p_end_returndate):
        archiveRec = db.session.query(ArchiveRecord)

        if p_start_referdate is not None:
            archiveRec = archiveRec.filter_by(p_start_referdate <= ArchiveRecord.referdate)

        if p_end_referdate is not None:
            archiveRec = archiveRec.filter_by(p_end_referdate >= ArchiveRecord.referdate)

        if p_archiveNum is not None:
            archiveRec = archiveRec.filter_by(archiveNum = p_archiveNum)

        if p_owner is not None:
            archiveRec = archiveRec.filter_by(owner = p_owner)

        if p_user is not None:
            archiveRec = archiveRec.filter_by(user = p_user)

        if p_status is not None:
            archiveRec = archiveRec.filter_by( status = p_status)

        if p_start_returndate is not None:
            archiveRec = archiveRec.filter_by(p_start_returndate < ArchiveRecord.returndate)

        if p_end_returndate is not None:
            archiveRec = archiveRec.filter_by(p_end_returndate < ArchiveRecord.returndate)

        archives = archiveRec.all()
        return archives
