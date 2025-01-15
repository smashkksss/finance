from fredapi import Fred

# Initialize with your FRED API key
fred = Fred(api_key='fc6a1301d2fdb5e253dbc0c')

# Example: Fetch the Consumer Price Index for All Urban Consumers
series_id = 'CPIAUCSL'
data = fred.get_series(series_id)
print(data.head())
