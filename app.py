from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"


    # Read the image from the request body
    image = request.files["image"].read()

    # Create a 3D model from the image
    model = create_model_from_image(image)

    # Save the 3D model
    with open("model.fbx", "wb") as f:
        f.write(model)

    return {"message": "The 3D model has been created."}

if __name__ == "__main__":
    app.run()
