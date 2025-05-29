import datetime
from typing import Union

def format_timestamp(timestamp: Union[str, float]) -> str:
    """Format timestamp to human-readable date"""
    if isinstance(timestamp, str):
        dt = datetime.datetime.fromisoformat(timestamp)
    else:
        dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def validate_age(age: str) -> bool:
    """Validate age input (0-150)"""
    try:
        return 0 <= int(age) <= 150
    except ValueError:
        return False

def resource_path(relative_path: str) -> Path:
    """Get absolute path to resource for PyInstaller compatibility"""
    base_path = Path(__file__).parent.parent
    return base_path / relative_path