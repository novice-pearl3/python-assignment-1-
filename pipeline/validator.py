# milestone 1

from datetime import datetime

def validate_record(record):

    if record["branch_id"] == "":
        return False
    
    if record["revenue"] < 0: 
        return False 


    try: 
        datetime.strptime(record["date"],"%Y-%m-%d")
    except ValueError:
        return False
    
    return True

