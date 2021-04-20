#CONSTANTS
import inspect
from datetime import datetime

# Application URL
URL = "https://opensource-demo.orangehrmlive.com/"

# Admin Credentials
ADMIN_USERNAME = "Admin"
ADMIN_PASSWORD = "admin123"

# CEO Credentials
CEO_USERNAME = "anroy1"
CEO_PASSWORD = "admin123"

# User Credentials
FIRSTNAME = "Anup2"
LASTNAME = "Roy2"

def func_name():
    return inspect.stack()[1][3]

def get_current_date_time():
    return datetime.today().strftime('%m:%d:%Y-%H:%M:%S')





