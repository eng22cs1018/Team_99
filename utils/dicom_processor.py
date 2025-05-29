import pydicom
import numpy as np
from PIL import Image

def read_dicom_file(file_path: str) -> dict:
    """Read DICOM file and return metadata + pixel data"""
    ds = pydicom.dcmread(file_path)
    
    metadata = {
        "patient_name": getattr(ds, "PatientName", ""),
        "patient_id": getattr(ds, "PatientID", ""),
        "study_date": getattr(ds, "StudyDate", ""),
        "modality": getattr(ds, "Modality", ""),
        "image_size": ds.pixel_array.shape
    }
    
    pixel_array = ds.pixel_array
    return {
        "metadata": metadata,
        "pixel_data": pixel_array
    }

def normalize_dicom_image(pixel_array: np.ndarray) -> Image.Image:
    """Normalize DICOM pixel data to 8-bit PNG"""
    img_array = pixel_array.astype(float)
    img_array = (img_array - np.min(img_array)) / np.ptp(img_array) * 255.0
    return Image.fromarray(img_array.astype(np.uint8))

def extract_measurements(dicom_data: dict) -> dict:
    """Extract clinical measurements from DICOM tags"""
    return {
        "ef": float(getattr(dicom_data, "LVEF", 0.0)),
        "lv_size": float(getattr(dicom_data, "LVSize", 0.0)),
        "rv_function": getattr(dicom_data, "RVFunction", "Normal")
    }