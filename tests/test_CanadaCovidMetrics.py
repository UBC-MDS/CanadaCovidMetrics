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


def test_total_cumulative_vaccine_completion():
    """Test total_cumulative_vaccine_completion"""

    # Test defaults return a dataframe object
    assert isinstance(ccm.total_cumulative_vaccine_completion(), pd.DataFrame), 'Pandas DataFrame Not Returned'

    # Test default call returns non-empty dataframe object
    assert ccm.total_cumulative_vaccine_completion().empty == False, 'Default returned dataframe is empty'

    # Test defaults returns expected dataframe components
    assert (ccm.total_cumulative_vaccine_completion().columns == [
        'cumulative_cvaccine',
        'cvaccine',
        'date_vaccine_completed',
        'province'
        ]).all(), 'Default returned dataframe has incorrect column names'

    # Test correct data is returned when date is specified
    df = ccm.total_cumulative_vaccine_completion(loc='QC', date='2021-05-01')  
    assert df['cumulative_cvaccine'].sum() == 97108, 'Incorrect cumulative_cvaccine returned when date is specified' 
    assert df['cvaccine'].sum() == 11250, 'Incorrect cvaccine returned when date is specified' 
    assert df['date_vaccine_completed'][0] == '01-05-2021', 'Incorrect date_vaccine_completed returned when data is specified' 
    assert df['province'][0] == 'Quebec', 'Incorrect province returned when date is specified' 
