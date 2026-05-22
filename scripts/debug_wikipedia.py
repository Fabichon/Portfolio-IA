import wikipedia
import requests

def diagnostic():
    print("--- Diagnostic Wikipedia API ---")
    try:
        # Test 1: Simple request via requests to check connectivity
        print("Test 1: Connection brute à l'API...")
        r = requests.get("https://en.wikipedia.org/w/api.php?action=query&format=json&titles=Main_Page")
        print(f"Status Code: {r.status_code}")
        print(f"Response Headers: {r.headers.get('Content-Type')}")
        r.json() # Should work
        print("✓ Connexion brute OK")
    except Exception as e:
        print(f"✗ Échec connexion brute: {e}")

    try:
        # Test 2: wikipedia library
        print("\nTest 2: Librairie 'wikipedia'...")
        wikipedia.set_lang("en")
        # Wikipedia recommends setting a user agent
        # wikipedia.set_user_agent("MyPortfolioApp/1.0 (contact@example.com)")
        page = wikipedia.page("Python (programming language)", auto_suggest=False)
        print(f"✓ Titre trouvé: {page.title}")
    except Exception as e:
        print(f"✗ Échec librairie 'wikipedia': {e}")

if __name__ == "__main__":
    diagnostic()
