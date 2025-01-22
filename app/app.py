from flask import Flask, request, jsonify
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import threading
import requests  # For Ollama API calls

# Flask app
app = Flask(__name__)

# Ollama API URL
OLLAMA_API_URL = "http://localhost:11434/api/chat"

# Function to interact with Ollama using Llama 3.2:1b
def respond_to_user_input_ollama(user_input):
    """
    Send user input to the Ollama API using the Llama 3.2:1b model and get the response.
    """
    try:
        headers = {"Content-Type": "application/json"}
        payload = {
            "model": "llama-3.2:1b",  # Specify the model
            "messages": [{"role": "user", "content": user_input}]
        }
        response = requests.post(OLLAMA_API_URL, json=payload, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses

        # Extract and return the response content
        return response.json()["choices"][0]["content"].strip()
    except requests.exceptions.RequestException as e:
        print(f"[Error] Ollama API request failed: {e}")
        return "I'm having trouble connecting to the AI. Please try again later."

# Flask route to handle AI responses
@app.route("/api/respond", methods=["POST"])
def api_respond():
    """
    Flask API endpoint to process user input and return AI responses.
    """
    data = request.json
    user_input = data.get("user_input", "")
    if not user_input:
        return jsonify({"error": "User input is required"}), 400

    response = respond_to_user_input_ollama(user_input)
    return jsonify({"response": response})

# Create a 3D avatar model
def create_avatar(radius=1.0, slices=32, stacks=32):
    """
    Create a 3D sphere to represent the avatar.
    :param radius: Radius of the sphere.
    :param slices: Number of slices for sphere tessellation.
    :param stacks: Number of stacks for sphere tessellation.
    """
    def draw_sphere():
        quad = gluNewQuadric()
        gluSphere(quad, radius, slices, stacks)
        gluDeleteQuadric(quad)
    return draw_sphere

# OpenGL and pygame rendering
def render_avatar():
    """
    Render the 3D avatar and allow user interaction via the console.
    """
    # Initialize the pygame window for OpenGL rendering
    pygame.init()
    screen = pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("3D Avatar with Llama 3.2 AI")
    gluPerspective(45, (800 / 600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    # Create the avatar
    avatar_model = create_avatar()

    print("Press 'Q' to quit the rendering window.")

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Handle user input
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    print("Quitting the application.")
                    running = False

        # Clear screen and render the avatar
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glPushMatrix()
        avatar_model()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

# Start the Flask server in a separate thread
def start_flask():
    """
    Start the Flask server in a new thread.
    """
    app.run(host="0.0.0.0", port=5000, debug=False)

if __name__ == "__main__":
    # Start the Flask server in a separate thread
    flask_thread = threading.Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    # Start the OpenGL rendering
    render_avatar()
