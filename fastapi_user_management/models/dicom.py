from sqlalchemy import Column, Integer, String
from fastapi_user_management.models.base import Base


class DicomSeries(Base):
    __tablename__ = "dicom_series"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, index=True)
    study_instance_uid = Column(String)
    series_instance_uid = Column(String)
    modality = Column(String)
    body_part_examined = Column(String)
