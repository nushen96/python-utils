import requests

url = "https://pen-to-print-handwriting-ocr.p.rapidapi.com/recognize/"

payload = "-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"srcImg\"\r\n\r\n\r\n-----011000010111000001101001\r\nContent-Disposition: form-data; name=\"Session\"\r\n\r\nstring\r\n-----011000010111000001101001--\r\n\r\n"
headers = {
    'content-type': "multipart/form-data; boundary=---011000010111000001101001",
    'x-rapidapi-key': "5c63a6b286mshe6dc0e3181e2fa7p1b3764jsn21868621f182",
    'x-rapidapi-host': "pen-to-print-handwriting-ocr.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)