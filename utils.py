from datetime import datetime,timedelta 

class utils:

    #add days to date
    def add_days_to_date(to = None, nDays=1):
        if to is None:
            to = datetime.now()
        date = to + timedelta(days=nDays*-1)
        return date

    def set_to_string(list):
        separator = '\''
        variable = '\',\''.join(list)
        return separator + variable+ separator