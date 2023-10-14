#!/usr/bin/python3
"""
This model creates a storage instance for attributes
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
