import datetime
import forecastio
import googlemaps

"""
Run load_forecast() with the given lat, lng, and time arguments.
"""
gmaps = googlemaps.Client(key='AIzaSyCMRyoXahIXK4exUlA7pe1wjpnWZUFZ4BM')

# Geocoding and address
geocode_result = gmaps.geocode('bangalore')
    
api_key = "42c20139ea8fac189a494795e7182eb9"
print(geocode_result[0]['geometry']['location']['lat'])
print(geocode_result[0]['geometry']['location']['lng'])
lat = geocode_result[0]['geometry']['location']['lat']
lng = geocode_result[0]['geometry']['location']['lng']
time = datetime.datetime(2016, 04, 13)

forecast = forecastio.load_forecast(api_key, lat, lng, time=time,lazy='false')
    
print("===========Currently Data=========")
print(forecast.currently())
"""
print "===========Hourly Data========="
by_hour = forecast.hourly()
print(by_hour)
print "Hourly Summary: %s" % (by_hour.summary)
    

for hourly_data_point in by_hour.data:
    print hourly_data_point.temperature,hourly_data_point.time,hourly_data_point.precipProbability,hourly_data_point.icon
"""
print("===========Daily Data=========")
by_day = forecast.daily()
print("Daily Summary: %s"  % (by_day.summary))

for daily_data_point in by_day.data:
    print(daily_data_point)
