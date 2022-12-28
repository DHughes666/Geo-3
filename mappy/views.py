from django.shortcuts import render
import folium
import geocoder 

from .models import Search

# Create your views here.
def index(request):
    address = request.POST.get('addre')
    location = geocoder.osm(address)
    #lat = location['latitude']
    lat = location.lat
    lng = location.lng
    country = location.country
    # Create Map Object
    m = folium.Map(location=[6.5244, 3.3792], zoom_start=2)
    folium.Marker([lat, lng], 
                  tooltip='Click for more',
                  popup=country).add_to(m)
    
    # Get HTML Representation of map object
    map = m._repr_html_()
    context = {'map': map}
    return render(request, 'mappy/main.html', context)