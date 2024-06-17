import qrcode

def generate_qr_code(url, file_name):
   
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_H,  
        box_size=10,  
        border=4, 
    )
    qr.add_data(url)
    qr.make(fit=True)

  
    img = qr.make_image(fill='black', back_color='white')
    
    img.save(file_name)
    print(f"QR Code generato con successo e salvato come '{file_name}'.")


website_url = "https://simonx.dev/"
qr_code_file = "qr_code_simonx_dev.png"


generate_qr_code(website_url, qr_code_file)

