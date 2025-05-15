from abc import ABC, abstractmethod
from typing import List, Dict

class AbstractReport(ABC):
    """Base class for all reports."""
    
    @classmethod
    @abstractmethod
    def generate(cls, employees: List[Dict]) -> List:
        """Report generation.
        
        Args:
            employees: List of dictionaries with employee data
            
        Returns:
            Line with the finished report
        """
        pass

    @classmethod
    @abstractmethod
    def get_name(cls) -> str:
        """Returns the name of the report."""
        pass