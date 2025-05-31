# Web-Scraping
--- /dev/null
+++ b/README.md
@@ -0,0 +1,109 @@
+# Récupérateur de Restaurants via Google Maps API / Restaurant Scraper via Google Maps API
+
+## Français 🇫🇷
+
+Ce script Python utilise l'API Google Places pour rechercher des restaurants dans des zones géographiques prédéfinies (principalement au Sénégal dans cet exemple) et enregistre les informations détaillées dans un fichier CSV.
+
+### Fonctionnalités
+
+*   Recherche de restaurants à proximité de coordonnées géographiques spécifiques (latitude, longitude) dans un rayon défini.
+*   Récupération d'informations détaillées pour chaque restaurant trouvé, y compris :
+    *   Nom
+    *   Adresse (peut être l'adresse approximative ou l'adresse formatée si disponible)
+    *   Note (si disponible)
+    *   Coordonnées géographiques (latitude, longitude)
+    *   Numéro de contact (international ou formaté, si disponible)
+    *   Site web (si disponible)
+*   Gestion de la pagination pour récupérer tous les résultats disponibles.
+*   Sauvegarde des données collectées dans un fichier CSV nommé `restaurants_senegal.csv`.
+*   Affichage de l'état du traitement et des erreurs potentielles de l'API dans la console.
+
+### Prérequis
+
+*   Python 3.x
+*   La bibliothèque `requests` : installez-la avec `pip install requests`.
+
+### Configuration
+
+1.  **Clé API Google Places** :
+    *   Vous devez obtenir une clé API Google Places auprès de la Google Cloud Platform Console.
+    *   Assurez-vous que l'API "Places API" est activée pour votre projet.
+    *   Remplacez la valeur de la variable `API_KEY` dans le script `main.py` par votre propre clé API.
+        ```python
+        API_KEY = 'VOTRE_CLE_API_ICI'
+        ```
+    *   **Important** : La clé API fournie dans le code d'origine (`AIzaSyB61CsFlwZ6XZTYd2S4p6BifWj_Av6Dwv0`) est un exemple et ne doit **PAS** être utilisée. Elle est probablement invalide ou soumise à des restrictions. L'utilisation d'une clé API valide est cruciale pour le fonctionnement du script.
+
+2.  **Zones de recherche** :
+    *   La variable `zones` dans `main.py` contient une liste de dictionnaires, chacun représentant une zone à scanner. Vous pouvez modifier cette liste pour cibler différentes villes ou quartiers. Chaque dictionnaire doit contenir `ville`, `quartier`, `lat` (latitude), et `lng` (longitude).
+
+3.  **Rayon de recherche** :
+    *   La variable `radius` (en mètres) définit la zone de recherche autour de chaque point central. Ajustez cette valeur selon vos besoins.
+
+### Utilisation
+
+1.  Assurez-vous d'avoir configuré votre clé API et les zones de recherche comme décrit ci-dessus.
+2.  Exécutez le script depuis votre terminal :
+    ```bash
+    python main.py
+    ```
+3.  Le script commencera à interroger l'API Google Places pour chaque zone et à écrire les données dans `restaurants_senegal.csv`.
+4.  Un message "✅ Fichier CSV généré : restaurants_senegal.csv" s'affichera à la fin du processus.
+
+### Avertissements
+
+*   L'utilisation de l'API Google Places est soumise à des quotas d'utilisation et peut entraîner des coûts. Surveillez votre consommation dans la Google Cloud Platform Console.
+*   Le script inclut des délais (`time.sleep`) pour éviter de surcharger l'API, mais soyez conscient des limites de taux.
+
+---
+
+## English 🇬🇧
+
+This Python script uses the Google Places API to search for restaurants in predefined geographical areas (primarily in Senegal in this example) and saves detailed information into a CSV file.
+
+### Features
+
+*   Searches for restaurants near specific geographic coordinates (latitude, longitude) within a defined radius.
+*   Retrieves detailed information for each restaurant found, including:
+    *   Name
+    *   Address (can be vicinity or formatted address if available)
+    *   Rating (if available)
+    *   Geographic coordinates (latitude, longitude)
+    *   Contact number (international or formatted, if available)
+    *   Website (if available)
+*   Handles pagination to retrieve all available results.
+*   Saves collected data to a CSV file named `restaurants_senegal.csv`.
+*   Displays processing status and potential API errors in the console.
+
+### Prerequisites
+
+*   Python 3.x
+*   The `requests` library: install it with `pip install requests`.
+
+### Configuration
+
+1.  **Google Places API Key**:
+    *   You need to obtain a Google Places API key from the Google Cloud Platform Console.
+    *   Ensure the "Places API" is enabled for your project.
+    *   Replace the value of the `API_KEY` variable in the `main.py` script with your own API key.
+        ```python
+        API_KEY = 'YOUR_API_KEY_HERE'
+        ```
+    *   **Important**: The API key provided in the original code (`AIzaSyB61CsFlwZ6XZTYd2S4p6BifWj_Av6Dwv0`) is an example and should **NOT** be used. It is likely invalid or restricted. Using a valid API key is crucial for the script to work.
+
+2.  **Search Zones**:
+    *   The `zones` variable in `main.py` contains a list of dictionaries, each representing an area to scan. You can modify this list to target different cities or neighborhoods. Each dictionary must contain `ville` (city), `quartier` (district/neighborhood), `lat` (latitude), and `lng` (longitude).
+
+3.  **Search Radius**:
+    *   The `radius` variable (in meters) defines the search area around each central point. Adjust this value as needed.
+
+### Usage
+
+1.  Ensure you have configured your API key and search zones as described above.
+2.  Run the script from your terminal:
+    ```bash
+    python main.py
+    ```
+3.  The script will start querying the Google Places API for each zone and writing data to `restaurants_senegal.csv`.
+4.  A message "✅ Fichier CSV généré : restaurants_senegal.csv" (✅ CSV file generated: restaurants_senegal.csv) will be displayed upon completion.
+
+### Warnings
+
+*   Usage of the Google Places API is subject to usage quotas and may incur costs. Monitor your usage in the Google Cloud Platform Console.
+*   The script includes delays (`time.sleep`) to avoid overwhelming the API, but be mindful of rate limits.
+
