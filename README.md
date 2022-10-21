# MONKEYPOX Dataset

This data set is based off of various data sets

1. USA - CDC https://www.cdc.gov/poxvirus/monkeypox/response/2022/mpx-trends.html
2. MD - Maryland Department of Health's Monkeypox Dashboard located at https://health.maryland.gov/phpa/OIDEOR/Pages/monkeypox.aspx

## Maryland Notes
*  MDH is not reporting counts in counties with fewer than 10 cases due to patient confidentiality
*  The Maryland Department of Health provides human monkeypox data reporting every Friday
*  All data are preliminary and subject to change based on additional reporting. Case and vaccine data reflect Maryland residents only. MDH is continuously evaluating its data and reporting systems and will make updates as more data becomes available.

## USA Notes
* Vaccine Data is only showing data from 56 jurisdictions (Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, District of Columbia, Florida, Georgia, Hawaii, Idaho, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Maine, Mariana Islands, Maryland, Massachusetts, Michigan, Minnesota, Mississippi, Missouri, Montana, Nebraska, Nevada, New Hampshire, New Jersey, New Mexico, New York, New York City, North Carolina, North Dakota, Ohio, Oklahoma, Oregon, Pennsylvania, Philadelphia, Puerto Rico, Rhode Island, South Carolina, South Dakota, Tennessee, Texas, Utah, Vermont, Virgin Islands, Virginia, Washington, West Virginia, Wisconsin, Wyoming). Additional jurisdictions are onboarded but have not administered any doses of vaccine: Republic of Palau, American Samoa, Federated States of Micronesia, Marshall Islands.
* Total vaccine doses administered data (TotalVaccineDosesAdministered.csv) are updated every Wednesday as soon as they are reviewed and verified
* Total Cases (CasesbyDate.csv) over time in the USA are updated every Wednesday as soon as they are reviewed and verified.
* Total Cases overtime per State (CasesByState.csv) is updated daily

## Global.Health
* Data pulled from https://github.com/globaldothealth/monkeypox/timeseries-confirmed.csv and https://github.com/globaldothealth/monkeypox/timeseries-country-confirmed.csv
* Data is no longer collected by Globa.Health

## WHO
* Data is pulled from Our World in data via their git repo - https://github.com/owid/monkeypox (https://github.com/owid/monkeypox/blob/main/owid-monkeypox-data.csv)
* The data is collected hourly as reported by WHO
* OWID has provided python scripts which will be investigated
