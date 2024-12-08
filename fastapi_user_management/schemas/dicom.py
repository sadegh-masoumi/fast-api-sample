from pydantic import BaseModel


class DicomSeriesBase(BaseModel):
    """Base schema for DICOM metadata.

    Represents the fields of the dicom_series table to validate data for creating or retrieving DICOM metadata.
    """
    patient_id: str
    study_instance_uid: str
    series_instance_uid: str
    modality: str
    body_part_examined: str
    
    model_config = {
        "orm_mode": True,
    }


class DicomSeriesCreate(DicomSeriesBase):
    """Schema for creating new DICOM entries."""

    # Additional fields for creating a new record (if any) can be added here


class DicomSeries(DicomSeriesBase):
    """Schema for DICOM entry response.

    Represents the schema that will be returned to the client after inserting a record.
    It may include a database-generated field such as an ID.
    """

    id: int

    model_config = {
        "orm_mode": True,
    }
