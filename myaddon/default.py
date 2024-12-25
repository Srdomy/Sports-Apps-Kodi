import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import os
import requests

def authenticate_user():
    """Chiede all'utente di inserire username e password."""
    dialog = xbmcgui.Dialog()
    username = dialog.input("Inserisci username:", type=xbmcgui.INPUT_ALPHANUM)
    password = dialog.input("Inserisci password:", type=xbmcgui.INPUT_ALPHANUM, option=xbmcgui.PASSWORD_VERIFY)

    # Verifica username e password
    if username == "Pezz8" and password == "DomTV10":
        return True
    else:
        dialog.ok("Errore", "Username o password errati")
        return False

def detect_device():
    """Chiede all'utente su quale dispositivo si trova."""
    dialog = xbmcgui.Dialog()
    options = ["Fire Stick", "Android TV"]
    choice = dialog.select("Seleziona il dispositivo:", options)

    if choice == 0:  # Fire Stick
        return "https://www.amazon.com/AFTVnews-com-Downloader/dp/B01N0BP507?dplnkId=3a36e98d-956e-453b-96d0-bb149e675627"
    elif choice == 1:  # Android TV
        return "https://play.google.com/store/apps/details?id=com.esaba.downloader"
    else:
        dialog.ok("Errore", "Nessun dispositivo selezionato.")
        return None

def install_downloader(device_url):
    """Installa Downloader in base al dispositivo."""
    if device_url:
        dialog = xbmcgui.Dialog()
        dialog.ok("Downloader", "Verrà aperto il link per scaricare Downloader.")
        xbmc.executebuiltin(f'RunAddon(script.module.webbrowser)')
        xbmc.executebuiltin(f'ActivateWindow(Browser,{device_url})')

def main_menu():
    """Mostra il menu principale per la selezione tra Sportsfire e Sport App."""
    dialog = xbmcgui.Dialog()
    options = ["Sportsfire", "Sport App"]
    choice = dialog.select("Scegli un'opzione:", options)

    if choice == 0:  # Sportsfire
        open_downloader_with_code("119368")
    elif choice == 1:  # Sport App
        device_url = detect_device()
        install_downloader(device_url)
        open_downloader_with_code("827894")
    else:
        dialog.ok("Esci", "Nessuna opzione selezionata.")

def open_downloader_with_code(code):
    """Apre Downloader con un codice specifico."""
    xbmc.executebuiltin(f'RunAddon(script.module.downloader)')
    dialog = xbmcgui.Dialog()
    dialog.ok("Downloader", f"Inserisci il codice: {code}")

def run():
    """Avvia il plugin."""
    if authenticate_user():
        main_menu()

if __name__ == "__main__":
    run()
