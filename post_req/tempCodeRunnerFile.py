response = requests.post(url = pixel_endpoint, json=pixel_parameters, headers=headers)
print(response.text)