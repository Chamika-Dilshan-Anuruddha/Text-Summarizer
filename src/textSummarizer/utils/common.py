import os
from box.exceptions import BoxValueError
import yaml
from box import ConfigBox
from pathlib import Path
from typing import Any
from textSummarizer.logging import logger

def read_yaml(path:Path)->ConfigBox:
    try:
        with open(path) as f:
            content=yaml.safe_load(f)
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


def create_directories(paths:list, verbose=True):
    try:
        for path in paths:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory at: {path}")
    except Exception as e:
        raise e


def get_size(path:Path)->str:
    try:
        size_in_kb=round(os.path.getsize(path)/1024)
        return f"~ {size_in_kb} KB"
    except Exception as e:
        raise e