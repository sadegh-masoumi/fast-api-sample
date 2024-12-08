from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session
import pydicom
from io import BytesIO

from fastapi_user_management.core.database import get_db
from fastapi_user_management.models.dicom import DicomSeries
from fastapi_user_management.schemas.dicom import DicomSeriesCreate

router = APIRouter(
    prefix="/dicom",
    tags=["dicom"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal Server Error"}
    },
)


@router.post("/upload")
async def upload_dicom_file(
    file: UploadFile = File(...), db: Session = Depends(get_db)
):
    """Endpoint to upload a DICOM file and store its metadata in the database.

    Args:
        file (UploadFile): DICOM file to upload
        db (Session, optional): Database session

    Raises:
        HTTPException: If the file is not a valid DICOM file or required metadata is missing.
    """
    try:
        # Read the uploaded file as bytes
        dicom_file = await file.read()

        # Use pydicom to read the file
        dicom_data = pydicom.dcmread(BytesIO(dicom_file))

        # Extract required DICOM fields
        patient_id = dicom_data.get("PatientID")
        study_instance_uid = dicom_data.get("StudyInstanceUID")
        series_instance_uid = dicom_data.get("SeriesInstanceUID")
        modality = dicom_data.get("Modality")
        body_part_examined = dicom_data.get("BodyPartExamined")

        # Check if all required fields are present
        if not all(
            [
                patient_id,
                study_instance_uid,
                series_instance_uid,
                modality,
                body_part_examined,
            ]
        ):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Missing required DICOM metadata",
            )

        # Store the metadata in the database
        dicom_series = DicomSeries(
            patient_id=patient_id,
            study_instance_uid=study_instance_uid,
            series_instance_uid=series_instance_uid,
            modality=modality,
            body_part_examined=body_part_examined,
        )
        db.add(dicom_series)
        db.commit()

        return {"message": "DICOM file uploaded and metadata stored successfully."}

    except Exception as e:
        raise HTTPException(
            status_code=400, detail="Error processing DICOM file: " + str(e)
        )
