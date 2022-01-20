from CanadaCovidMetrics import CanadaCovidMetrics as ccm
import pytest
import pandas as pd

def test_date_format_check():
    """Test date_format_check"""

    # initialise values to test
    date_correct_format = "2021-10-31"
    date_wrong_format = "10-31-2021"
    not_a_date = "121242539"

    # expect None returned for proper date format
    assert ccm.date_format_check(date_correct_format) == None
    
    # expect ValueError raised for incorrect date format
    with pytest.raises(ValueError):
        ccm.date_format_check(date_wrong_format)
    
    with pytest.raises(ValueError):
        ccm.date_format_check(not_a_date)

def test_loc_format_check():
    """Test loc_format_check"""

    # initialise values to test
    loc_correct_format = "canada"
    loc_wrong_format = "PEI"
    not_a_loc = "ABC1234!"

    # expect None returned for proper loc format
    assert ccm.loc_format_check(loc_correct_format) == None
    
    # expect ValueError raised for incorrect loc format
    with pytest.raises(ValueError):
        ccm.loc_format_check(loc_wrong_format)
    
    with pytest.raises(ValueError):
        ccm.loc_format_check(not_a_loc)

def test_total_cumulative_recovered_cases():
    """Test loc_format_check"""

    # check default call returns a dataframe object
    assert isinstance(ccm.total_cumulative_recovered_cases(), pd.DataFrame)

    # check default call returns non-empty dataframe object
    assert ccm.total_cumulative_recovered_cases().empty == False
    
    # check default call returns expected dataframe components
    assert (ccm.total_cumulative_recovered_cases().columns == [
        'cumulative_recovered',
        'date_recovered',
        'province',
        'recovered'
        ]).all()


def test_total_cumulative_deaths():
    """Test total_cumulative_deaths"""

    # Test correct data is returned when date is specified
    data = [[1078, '18-01-2021', 31, 'BC']]
    df = pd.DataFrame(data, columns = ['cumulative_deaths', 'date_death_report', 'death', 'province'])
    assert df['cumulative_deaths'].sum() == 1078
    assert df['death'].sum() == 31
    
    # Test correct data is returned when date is not specified
    df = ccm.total_cumulative_deaths(loc='BC', date=None, after='2020-01-01', before = '2020-07-30')
    assert df['deaths'].sum() == 194

    # Test correct data size is returned
    df = ccm.total_cumulative_deaths(loc='BC', date=None, after='2020-01-01', before = '2020-10-30')
    assert df.shape == (237, 4)