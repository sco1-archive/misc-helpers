from datetime import datetime
import itertools

def drange(instr, datefmt='%Y-%m-%d'):
    """
    Generate a list of dates given an input date string with wildcards '*'

    e.g. datestrlist = [date for date in drange('2018-01-1*')]

    Will yield: ["2018-01-20","2018-01-21", ..... ,"2018-01-29"]

    Multiple wildcards are supported, as should most numeric date formats (untested)
    """
    staridx = [idx for idx, char in enumerate(instr) if char == '*']
    
    for comb in itertools.product('0123456789', repeat=len(staridx)):
        # Plug the combination into the wildcard(s)
        tmplist = list(instr)
        for idx, digitstr in enumerate(comb):
            tmplist[staridx[idx]] = digitstr
        teststr = "".join(tmplist)
        try:
            # Use datetime to validate whether it's a date
            datetimetest = datetime.strptime(teststr, datefmt)
            yield datetimetest.strftime(datefmt)
        except ValueError as err:
            # ValueError most likely means that we've given it an invalid date
            # This *could* fail for other reasons, so be careful
            continue