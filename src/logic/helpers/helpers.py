from os import system, name
from os.path import join
from json import load, dump

__all__ = [
    "cc"
]

def cc():
    system("cls" if name == "nt" else "clear")

class DataLoader:
    def __init__(self, *file_path: str) -> None:
        self.file_path = join(*file_path)
    
    def load_data(self) -> dict | list:
        try:
            with open(self.file_path, "r") as f:
                return load(f)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Filepath: {self.file_path} not found when loading {self.__class__.__qualname__}")
        
        except Exception as e:
            raise Exception(f"Exception raised in {self.__class__.__qualname__} when loading data: {e}")
    
    def save_data(self, data: dict | list) -> None:
        try:
            with open(self.file_path, "w") as f:
                dump(data, f, indent = 4)
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Filepath: {self.file_path} not found when saving in {self.__class__.__qualname__}")

        except Exception as e:
            raise Exception(f"Exception raised in {self.__class__.__qualname__} when saving data: {e}")
    

    