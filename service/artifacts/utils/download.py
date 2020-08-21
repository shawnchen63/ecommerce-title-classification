import requests

model_name_to_id = {
    "beautypipeline1.joblib" : '1p9G9a1dRgct8UEcduN8hTapNZyV7FeKC',
    "fashionpipeline1.joblib" : '1w6QJLK3KRl1WeuJZ0LXlFQzOXLLwyiIk',
    "mobilepipeline1.joblib" : '1G8BflXXmesS7169yyuYVTeahfIqJPNDK'
}

def download_file_from_google_drive(model_name, destination):

    URL = "https://docs.google.com/uc?export=download"
    gdrive_id = model_name_to_id[model_name]

    session = requests.Session()

    response = session.get(URL, params = { 'id' : gdrive_id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : gdrive_id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    print("Downloading to ", destination)

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

    print("Downloaded")

if __name__ == "__main__":
    model_name = 'beautypipeline1.joblib'
    destination = '/home/shawn/ecommerce-title-classification/service/artifacts/beautypipeline1.joblib'
    download_file_from_google_drive(model_name, destination)