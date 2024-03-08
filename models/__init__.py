#!/usr/bin/python3

"""
Init module for models runs everytime models is accessed
"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
