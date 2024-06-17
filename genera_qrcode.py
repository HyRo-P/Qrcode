import qrcode

def generate_qr_code(url, file_name):
    # Creazione dell'oggetto QRCode
    qr = qrcode.QRCode(
        version=1,  # Versione del QR Code (1-40)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # Livello di correzione degli errori (H = alta)
        box_size=10,  # Dimensione dei box nel QR Code
        border=4,  # Spessore del bordo del QR Code
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Creazione di un'immagine PIL
    img = qr.make_image(fill='black', back_color='white')

    # Salvataggio dell'immagine
    img.save(file_name)

    print(f"QR Code generato con successo e salvato come '{file_name}'.")

# URL del sito
website_url = "https://simonx.dev/"
# Nome del file del QR Code
qr_code_file = "qr_code_simonx_dev.png"

# Chiamata alla funzione per generare il QR Code
generate_qr_code(website_url, qr_code_file)

