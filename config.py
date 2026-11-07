from dotenv import find_dotenv,load_dotenv
import os
def getkey()->str:
    status=load_dotenv(
        find_dotenv(),override=True
    )
    return os.getenv('GOOGLE_API_KEY')
print(f"the scret key file is:{getkey()}")