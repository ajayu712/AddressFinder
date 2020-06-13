#Reverse Geocoding
#Finding Location Using Coordinates

from geopy import Nominatim
coord=[19.0779378,72.8869236]
geolocator = Nominatim(user_agent='test/1')
location = geolocator.reverse(f'{coord[0]},{coord[1]}')
print(location.address)