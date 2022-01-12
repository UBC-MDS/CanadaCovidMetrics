from datetime import date
import requests
import pandas as pd

"""
Sample format of a request 

url = 'https://api.opencovid.ca/timeseries?stat=cases&loc=prov&date=01-09-2020'
r = requests.get(url = url)
json_body = r.json()

convert to pd.DataFrame (optional?)

    - If we do this, we'll have to update the docstrings
    to specify that the functions return a pandas dataframe
"""

today = '{}'.format(date.today())

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
    dict
        JSON response from queried api.

    Examples
    --------
    >>> total_cumulative_recovered_cases(loc='BC')
    """

    return


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

