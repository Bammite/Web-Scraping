import requests
import csv
import time

API_KEY = 'AIzaSyB61CsFlwZ6XZTYd2S4p6BifWj_Av6Dwv0'

zones = [
    # Dakar
    {"ville": "Dakar", "quartier": "Plateau", "lat": 14.6681, "lng": -17.4399},
    {"ville": "Dakar", "quartier": "Medina", "lat": 14.6815, "lng": -17.4467},
    {"ville": "Dakar", "quartier": "Yoff", "lat": 14.7405, "lng": -17.4902},
    {"ville": "Dakar", "quartier": "Almadies", "lat": 14.7519, "lng": -17.5135},
    {"ville": "Dakar", "quartier": "Parcelles Assainies", "lat": 14.7640, "lng": -17.4291},
    {"ville": "Dakar", "quartier": "Guediawaye", "lat": 14.7845, "lng": -17.3853},
    {"ville": "Dakar", "quartier": "Rufisque", "lat": 14.7153, "lng": -17.2731},
    {"ville": "Dakar", "quartier": "Hann", "lat": 14.7178, "lng": -17.4302},
    {"ville": "Dakar", "quartier": "Mermoz", "lat": 14.6921, "lng": -17.4642},
    # Thiès
    {"ville": "Thiès", "quartier": "Thiès Nord", "lat": 14.8147, "lng": -16.9310},
    {"ville": "Thiès", "quartier": "Thiès Sud", "lat": 14.7904, "lng": -16.9265},
    {"ville": "Thiès", "quartier": "Grand Thiès", "lat": 14.8038, "lng": -16.9252},
    # Saint-Louis
    {"ville": "Saint-Louis", "quartier": "Centre-ville", "lat": 16.0240, "lng": -16.5086},
    {"ville": "Saint-Louis", "quartier": "Sor", "lat": 16.0218, "lng": -16.4920},
    {"ville": "Saint-Louis", "quartier": "Guet-Ndar", "lat": 16.0342, "lng": -16.5032},
    {"ville": "Saint-Louis", "quartier": "Ndar Toute", "lat": 16.0275, "lng": -16.5020},
]

radius = 2000  # Rayon de recherche en mètres

# Création du fichier CSV
with open('restaurants_senegal.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['ville', 'quartier', 'name', 'address', 'rating', 'lat', 'lng', 'contact', 'website']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for zone in zones:
        url = (
            f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
            f"location={zone['lat']},{zone['lng']}&"
            f"radius={radius}&"
            f"type=restaurant&"
            f"key={API_KEY}"
        )

        while url:
            res = requests.get(url)
            data = res.json()
            print(f"Traitement : {zone['ville']} - {zone['quartier']} | Status : {data.get('status')}")

            if data.get('status') != "OK":
                if data.get('error_message'):
                    print(f"Erreur API : {data.get('error_message')}")
                break

            for place in data.get('results', []):
                place_id = place.get('place_id')
                contact = ""
                website = ""
                address = place.get('vicinity')

                if place_id:
                    details_url = (
                        f"https://maps.googleapis.com/maps/api/place/details/json?"
                        f"place_id={place_id}&fields=formatted_phone_number,international_phone_number,website,formatted_address&key={API_KEY}"
                    )
                    details_res = requests.get(details_url)
                    details_data = details_res.json()
                    result = details_data.get('result', {})
                    contact = (
                        result.get('international_phone_number') or
                        result.get('formatted_phone_number') or
                        ""
                    )
                    website = result.get('website') or ""
                    address = result.get('formatted_address') or address

                row = {
                    'ville': zone['ville'],
                    'quartier': zone['quartier'],
                    'name': place.get('name'),
                    'address': address,
                    'rating': place.get('rating'),
                    'lat': place['geometry']['location']['lat'],
                    'lng': place['geometry']['location']['lng'],
                    'contact': contact,
                    'website': website
                }
                writer.writerow(row)
                csvfile.flush()
                time.sleep(0.1)  # Petite pause pour ne pas saturer l'API

            # Gestion de la pagination
            next_page_token = data.get('next_page_token')
            if next_page_token:
                time.sleep(2)  # Nécessaire pour activer le token
                url = (
                    f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?"
                    f"pagetoken={next_page_token}&key={API_KEY}"
                )
            else:
                url = None

print("✅ Fichier CSV généré : restaurants_senegal.csv")
