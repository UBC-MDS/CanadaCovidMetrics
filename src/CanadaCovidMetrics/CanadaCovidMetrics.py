import datetime as dt
from multiprocessing.sharedctypes import Value
import requests
import pandas as pd

today = '{}'.format(dt.date.today())
format_ymd = "%Y-%m-%d"
format_dmy = "%d-%m-%Y"
format_prov = ['canada', 'prov', 'BC', 'AB', 'SK', 'MB', 'ON', 'QC', 'NL', 'NB', 'NS', 'PE', 'NT', 'YT', 'NU', 'RP']

def total_cumulative_cases(loc='prov', date=None, after='2020-01-01', before=today):
    """Query total cumulative cases with ability to specify \
        location and date range of returned data.

    Parameters
    ----------
    loc : str
        Specify geographic filter and aggregation of returned data.
        Valid loc arguments are: 'canada', 'prov' and two-letter \
        province codes (e.g. 'ON', 'BC', etc.)
    date : str
        If not None, return data from the specified date YYYY-MM-DD.
        Superceeds 'after' and 'before' parameters.
    after : str
        Return data on and after the specified date YYYY-MM-DD.
    before : str
        Return data on and before the specified date YYYY-MM-DD.

    Returns
    -------
    dict
        JSON response from queried api.

    Examples
    --------
    >>> total_cumulative_cases(loc='BC')
    """

    return


def total_cumulative_deaths(loc='prov', date=None, after='2020-01-01', before=today):
    """Query total cumulative deaths with ability to specify \
        location and date range of returned data.

    Parameters
    ----------
    loc : str
        Specify geographic filter and aggregation of returned data.
        Valid loc arguments are: 'canada', 'prov' and two-letter \
        province codes (e.g. 'ON', 'BC', etc.)
    date : str
        If not None, return data from the specified date YYYY-MM-DD.
        Superceeds 'after' and 'before' parameters.
    after : str
        Return data on and after the specified date YYYY-MM-DD.
    before : str
        Return data on and before the specified date YYYY-MM-DD.

    Returns
    -------
    dict
        JSON response from queried api.

    Examples
    --------
    >>> total_cumulative_deaths(loc='BC')
    """

    return


def total_cumulative_recovered_cases(loc='prov', date=None, after='2020-01-01', before=today):
    """Query total cumulative recovered cases with ability \
        to specify location and date range of returned data.

    Parameters
    ----------
    loc : str
        Specify geographic filter and aggregation of returned data.
        Valid loc arguments are: 'canada', 'prov' and two-letter \
        province codes (e.g. 'ON', 'BC', etc.)
    date : str
        If not None, return data from the specified date YYYY-MM-DD.
        Superceeds 'after' and 'before' parameters.
    after : str
        Return data on and after the specified date YYYY-MM-DD.
    before : str
        Return data on and before the specified date YYYY-MM-DD.

    Returns
    -------
    df
        Pandas dataframe containing content of API response.

    Examples
    --------
    >>> total_cumulative_recovered_cases(loc='BC')
    """  
    if loc not in format_prov:
        raise(ValueError("Value passed for loc argument is not recognized. Must be one of: 'prov', 'canada', or a two-letter capitalized province code"))

    if date is not None:
        try:
            dt.datetime.strptime(date, format_ymd)
        except:
            try:
                dt.datetime.strptime(date, format_dmy)
            except:
                raise(ValueError("Incorrect date format {} : date format should be either YYYY-MM-DD or DD-MM-YYYY".format(date)))
        
        url = 'https://api.opencovid.ca/timeseries?stat=recovered&loc={}&date={}'.format(loc, date)
    
    else:
        try:
            dt.datetime.strptime(before, format_ymd)
        except:
            try:
                dt.datetime.strptime(before, format_dmy)
            except:
                raise(ValueError("Incorrect before-date format {} : date format should be either YYYY-MM-DD or DD-MM-YYYY".format(before)))
        
        try:
            dt.datetime.strptime(after, format_ymd)
        except:
            try:
                dt.datetime.strptime(after, format_dmy)
            except:
                raise(ValueError("Incorrect after-date format {} : date format should be either YYYY-MM-DD or DD-MM-YYYY".format(after)))

        url = 'https://api.opencovid.ca/timeseries?stat=recovered&loc={}&after={}&before={}'.format(loc, after, before)
    
    r = requests.get(url = url)
    json_body = r.json()['recovered']
    df = pd.DataFrame.from_dict(json_body)

    return df


def total_cumulative_vaccine_completion(loc='prov', date=None, after='2020-01-01', before=today):
    """Query total cumulative vaccine completion with ability \
        to specify location and date range of returned data.

    Parameters
    ----------
    loc : str
        Specify geographic filter and aggregation of returned data.
        Valid loc arguments are: 'canada', 'prov' and two-letter \
        province codes (e.g. 'ON', 'BC', etc.)
    date : str
        If not None, return data from the specified date YYYY-MM-DD.
        Superceeds 'after' and 'before' parameters.
    after : str
        Return data on and after the specified date YYYY-MM-DD.
    before : str
        Return data on and before the specified date YYYY-MM-DD.

    Returns
    -------
    dict
        JSON response from queried api.

    Examples
    --------
    >>> total_cumulative_vaccine_completion(loc='BC')
    """

    return

print(total_cumulative_recovered_cases())