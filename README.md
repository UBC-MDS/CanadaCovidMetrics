# CanadaCovidMetrics

This is a Python package that provides key metrics regarding COVID-19 situation in Canada across provinces using the [OpenCovid API](https://opencovid.ca/api/).

## Summary

This package allows users to obtain key metrics on COVID-19 situation in Canada at national or provincial level for a specific time period. The 4 functions will return key metrics, including total cumulative cases, total cumulative deaths, total cumulative recovered cases and total cumulative vaccine completion, using data from [OpenCovid API](https://opencovid.ca/api/). The users may use the key metrics to conduct further analyses on COVID-19 situation in Canada.

## Functions

There are 4 functions in this package:\

-   `total_cumulative_cases` Return cumulative COVID cases by province or at national level. User can specific the time period with start and end dates.

-   `total_cumulative_deaths` Return cumulative deaths by province or at national level. User can specific the time period with start and end dates.

-   `total_cumulative_recovered` Return cumulative recovered cases by province or at national level. User can specific the time period with start and end dates.

-   `total_cumulative_vaccine` Return cumulative vaccine completion by province or at national level. User can specific the time period with start and end dates.

## Python ecosystem

There are several packages for easy access to COVID-19 key metrics or data using different APIs, examples include\
- [covid](https://github.com/nf1s/covid) using [John Hopkins University API](https://coronavirus.jhu.edu/about/)\
- [COVID19Py](https://github.com/Kamaropoulos/COVID19Py) using [Coronavirus Tracker API](https://github.com/ExpDev07/coronavirus-tracker-api)\
- [covid19pyclient](https://github.com/NiklasTiede/covid19pyclient) using [RKI API](https://github.com/marlon360/rki-covid-api)

To our knowledge, there is no similar package using [OpenCovid API](https://opencovid.ca/api/) in the Python ecosystem.

## Contributors

-   Adam Morphy (@adammorphy)
-   Brandon Lam (@ming0701)
-   Lakshmi Santosha Valli Akella (@valli180)
-   Luke Collins (@lcolli01)

We welcome and recognize all contributions. Please find the guide for contribution in [Contributing Document](https://github.com/UBC-MDS/CanadaCovidMetrics/blob/main/CONTRIBUTING.md).
