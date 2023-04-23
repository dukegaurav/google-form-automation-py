from dotenv import load_dotenv
import os
import pandas as pd
import os
from datetime import datetime
import pytz
import random
load_dotenv()

APP_DATA = os.getenv("APPDATA")
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')
image_path = os.path.join(os.getcwd(), 'temp_image.png')
date = datetime.now(pytz.timezone('Asia/Kolkata'))

apprc_source_list = ['Facebook','Twitter','Google Review','Instagram']
apprc_source = random.choice(apprc_source_list)




# profile_path = rf'{APP_DATA}\Mozilla\Firefox\Profiles\ljlxdxn2.gaurav'
profiles = rf"{APP_DATA}\Mozilla\Firefox\Profiles"
profile_name = 'gaurav'


print(find_profile(profiles,profile_name))