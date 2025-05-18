# myapp/signals.py
from typing import final
import requests
#

# Token del bot di Telegram - API Telegram Bot
TELEGRAM_BOT_TOKEN: final = '###'
# ID del tuo canale o gruppo - 
TELEGRAM_CHAT_ID: final = '###'  

# Funzione sincrona per inviare un messaggio su Telegram
def send_telegram_message(username):
    message = f"L'utente [{username}] ha effettuato il login."
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message
    }

    try:
        response = requests.post(url, data=payload, timeout=10)
        
        if response.status_code == 200:
            print("✅ Messaggio Telegram inviato")
        else:
            print(f"❌ Errore nell'invio del messaggio: {response.status_code} - {response.text}")

    except requests.exceptions.Timeout:
        print("⏱️ Timeout: il server Telegram non ha risposto in tempo.")

    except requests.exceptions.ConnectionError:
        print("🔌 Errore di connessione: impossibile raggiungere Telegram.")

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Errore durante l'invio del messaggio: {e}")

#

# async -> usa httpx() -> HTTPX is a fully featured HTTP client library for Python 3 ==> invio/ricezione sms bot -> utente & utente -> bot
# sync -> usa requests.post() ==> invio sms bot -> utente