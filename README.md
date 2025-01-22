# 3D avatar and an LLM-based conversational AI

---

3D Avatar with Llama 3.2 Conversational AI

This project combines a 3D avatar with conversational AI powered by the **Llama 3.2 model** running on **Ollama**. The application uses OpenGL to render a 3D avatar and integrates the AI model for interactive conversations.

---

## Features

- **3D Avatar**: A simple 3D sphere rendered using PyOpenGL and Pygame.
- **Conversational AI**: Integrated with the Llama 3.2 model using the Ollama API for natural language interaction.
- **Dockerized Setup**: Fully containerized with Docker Compose, making it easy to deploy.

---

## Prerequisites

Before starting, ensure you have the following installed:

- **GPU**: You require a GPU attached to the server or system where you run this application.
- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Ollama**: [Install Ollama](https://ollama.ai/)

---

## Project Structure

```
project/
├── app/
│   ├── app.py                 # Main Python application
│   ├── Dockerfile             # Dockerfile for the Python app
│   ├── requirements.txt       # Python dependencies
├── docker-compose.yml         # Docker Compose configuration
├── README.md                  # Documentation (this file)
```

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd project
```

### 2. Start the Services
Use Docker Compose to build and start the services:
```bash
docker-compose up --build
```

### 3. Interact with the Application
- The **Ollama service** runs at `http://localhost:11434`.
- The **3D avatar application** will be interactive in the terminal or render a 3D sphere using OpenGL.

---

## Configuration

- **Ollama API URL**: The Python app communicates with the Ollama service using `OLLAMA_API_URL`. This is set to `http://ollama_service:11434/api/chat` in the `docker-compose.yml`.
- **Ports**:
  - Ollama API: `11434`
  - Python App (Optional): `5000` if exposed externally.

---

## Stopping the Services

To stop the running containers, use:
```bash
docker-compose down
```

---

## Troubleshooting

1. **Ollama API Not Accessible**:
   - Ensure the Ollama service is running locally or in the Docker container.
   - Verify the API endpoint: `http://localhost:11434`.

2. **Python Dependencies**:
   - If new dependencies are added, update `requirements.txt` and rebuild:
     ```bash
     docker-compose up --build
     ```

3. **3D Rendering Issues**:
   - Ensure OpenGL drivers are installed on your host system.

---

## Future Enhancements

- Add more complex 3D models and animations for the avatar.
- Improve conversational capabilities with fine-tuned models.
- Integrate a front-end interface for better user interaction.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [Ollama](https://ollama.ai/) for the Llama 3.2 model and API.
- [PyOpenGL](https://pyopengl.sourceforge.io/) for 3D rendering.
- [Pygame](https://www.pygame.org/) for window management and interactivity.

