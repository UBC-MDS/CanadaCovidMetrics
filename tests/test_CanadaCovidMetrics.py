from CanadaCovidMetrics import CanadaCovidMetrics
import datetime as dt
from multiprocessing.sharedctypes import Value
import requests
import pandas as pd

def test_total_cumulative_deaths():
    """Test total_cumulative_deaths"""

    # Test correct data is returned when date is specified
    data = [[1078, '18-01-2021', 31, 'BC']]
    df = pd.DataFrame(data, columns = ['cumulative_deaths', 'date_death_report', 'death', 'province'])
    assert df['cumulative_deaths'].sum() == 1078
    assert df['death'].sum() == 31
    
    # Test correct data is returned when date is not specified
    df = total_cumulative_deaths(loc='BC', date=None, after='2020-01-01', before = '2020-07-30')
    assert df['deaths'].sum() == 194

    # Test correct data size is returned
    df = total_cumulative_deaths(loc='BC', date=None, after='2020-01-01', before = '2020-10-30')
    assert df.shape == (237, 4)


def test_total_cummulative_cases():
    """ Test total_cummulative_cases"""
    
    # Test correct data is returned when date is specified
    data = [[17, 56, "25-01-2020", "Alberta"]]
    df = total_cumulative_cases(loc='AB', date='15-03-2020', after='2020-01-01', before=today)
    assert df['cumulative_cases'].sum() == 56, 'Incorrect data obtained!'
    assert df['cases'].sum() == 17, 'Incorrect data obtained!'
    
    #Test correct data is returned when date is not specified
    data = [[0, 0 ,'25-01-2020',"Alberta"]]
    df = pd.DataFrame(data, columns = ["cases", "cumulative_cases", "date_report", "province"])
    assert df['cumulative_cases'].sum() == 0, 'Incorrect data obtained!'
    assert df['cases'].sum() == 0, 'Incorrect data obtained!'
    
    
    #Test to check if every province data is returned for a given day when loc = "prov"
    
    df = total_cumulative_cases(loc='prov', date='15-03-2020', after='2020-01-01', before=today)
    assert df["province"].nunique() == 14, 'Incorrect data obtained!'
    
    # Test to check for the correct columns in the dataframe returned
    
    df = total_cumulative_cases(loc='AB', date='15-03-2020', after='2020-01-01', before=today)
    assert (df.columns == ['cases', 'cumulative_cases', 'date_report', 'province']).all(),  'Incorrect data obtained!'
    
  
    