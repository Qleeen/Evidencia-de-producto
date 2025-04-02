from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route("/")
def home():
    # Obtener una imagen de gatito de The Cat API
    response = requests.get("https://api.thecatapi.com/v1/images/search")
    cat_data = response.json()
    cat_image_url = cat_data[0]["url"]

    # HTML con la imagen del gato
    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gatito Aleatorio</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 50px;
            }
            img {
                max-width: 80%;
                height: auto;
                border-radius: 10px;
                box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            }
        </style>
    </head>
    <body>
        <h1>🐱 Aquí tienes un gatito aleatorio 🐱</h1>
        <img src="{{ image_url }}" alt="Gatito">
    </body>
    </html>
    """

    return render_template_string(html_template, image_url=cat_image_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
