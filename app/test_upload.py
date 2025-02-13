import requests

def test_upload():
    url = 'http://localhost:8000/uploadfile/'
    
    # Open the file in binary mode
    with open('spiderman.jpg', 'rb') as f:
        files = {'file': ('spiderman.jpg', f, 'image/jpeg')}
        
        response = requests.post(url, files=files)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")

if __name__ == "__main__":
    test_upload()