from pathlib import Path

def root_path() -> Path:
    return Path(__file__).parent

def database_dir() -> Path:
    return root_path().joinpath("App").joinpath("database")

def database() -> Path:
    return database_dir().joinpath("database.db")