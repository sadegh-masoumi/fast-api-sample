# FastAPI User Management

Since pydantic has a released version v2, there are some task we need to do for this project.

- [ ] Update from Pydantic v1 to v2
- [ ] Check for any major security leaks (like plain text password or token)
- [ ] Add **Phone Number** and **Last Login** columns to `user_account` table.
- [ ] Provide an endpoint for **User Profile**.
- [ ] Create an endpoint, so user can upload a [DICOM file](https://en.wikipedia.org/wiki/DICOM) and store these headers from uploaded file in database table called **dicom_series** (`PatientID`, `StudyInstanceUID`, `SeriesInstanceUID`, `Modality`, `BodyPartExamined`).
- [ ] Write tests for this code for future purposes (If you want to refactor code while writing test, you're free to do so.)
- [ ] Dockerize this project
