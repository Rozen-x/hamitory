# utils.py
import sys
import os
def resource_path(relative_path):
    """برای فایل‌های فقط خواندنی (عکس‌ها، صداها)"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def data_path(relative_path):
    """برای فایل‌هایی که باید خوانده و نوشته شوند (JSON, save files)"""
    # کنار فایل exe ذخیره می‌شود
    if getattr(sys, 'frozen', False):
        # داریم از exe اجرا می‌شویم
        base_path = os.path.dirname(sys.executable)
    else:
        # داریم از کد مستقیم اجرا می‌شویم
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)