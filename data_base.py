import json
import os
from utils import data_path  # از تابع data_path استفاده کنید

class DataBase:
    def __init__(self):
        self.path = "data_base.json"
        self.keys = [
            "is_first_time",
            "count_of_win",
            "count_of_lose"]
        
        # اگر فایل وجود نداشت، بسازید
        if not os.path.exists(data_path(self.path)):
            with open(data_path(self.path), "w", encoding="utf-8") as file:
                default_data = {
                    "is_first_time": True,
                    "count_of_win": 0,
                    "count_of_lose": 0
                }
                json.dump(default_data, file, ensure_ascii=False, indent=4)

    def set_data(self, key: str, value):
        if not key in self.keys:
            raise ValueError("key not exist!!")
        
        # بقیه بررسی‌ها...
        
        with open(data_path(self.path), "r", encoding="utf-8") as file:
            data = json.load(file)
            data[key] = value

        with open(data_path(self.path), "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
            
        
    def get_data(self, key):
        if not key in self.keys:
            raise ValueError("key not exist!!")
        with open(data_path(self.path), 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data[key]