from django.shortcuts import render
import json
import urllib.request

def index(request):
    data = {}
    if request.method == 'POST':
        city = request.POST['city']
        api_key = 'JWBA8ZBXQ4X7M7XQR9DG6HV7A'  # Your actual API key
        url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?key={api_key}'
        
        try:
            with urllib.request.urlopen(url) as response:
                source = response.read()
                list_of_data = json.loads(source)
                
                data = {
                    "city": city,
                    "temperature": list_of_data['days'][0]['temp'],
                    "description": list_of_data['days'][0]['description'],
                    "humidity": list_of_data['days'][0]['humidity'],
                    # Add more fields as needed
                }
        except urllib.error.HTTPError as e:
            data['error'] = f"HTTP Error: {e.code} - {e.reason}"
        except Exception as e:
            data['error'] = str(e)

    return render(request, 'index.html', data)
