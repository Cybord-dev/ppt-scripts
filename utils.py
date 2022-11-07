from datetime import datetime,timedelta 

class utils:

    #add days to date
    def addDaysToDate(to = None, nDays=1):
        if to is None:
            to = datetime.now()
        date = to + timedelta(days=nDays*-1)
        return date
