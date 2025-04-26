# AI Code Generator

AI Code Generator is a Flask-based web application that generates AI-powered Python code and a title that summarizes the code when users enter a prompt. The application is containerized with Docker and can be deployed on Kubernetes using Helm Chart. It offers an enhanced experience with its user-friendly interface, code cloning feature, and loading animation.

### Features

1-Prompt Based Code Generation: Generates Python code and summary header according to user prompt.

2-User Friendly Interface: Easy to use with a simple and modern web interface.

3-Code Copy: Ability to copy the generated code to the clipboard with a single click.

4-Loading Animation: Visual feedback during code generation.

5-Kubernetes Support: Easy deployment on Minikube or Kubernetes with Helm chart.

### Requirements

Requirements

```bash
Python: 3.8 or higher
pip: Python package manager
Docker: Create and run containers
Kubernetes: Minikube recommended
Helm: For Kubernetes deployment
```

## Instalation

1. Cloning the Repository

```bash
git clone <github_repo_url>
cd ai-kod-uretici
```

2. Configuring Environment Variables

```bash
OPENAI_API_KEY=your_openai_api_key
```

3. Load Dependencies

```bash
pip install -r requirements.txt
```

4.Run the Flask Application

```bash
python app.py
```

5.Running with Docker

```bash
docker build -t <dockerhub_username>/s4e-intern-devops:latest .
docker run -p 5000:5000 <dockerhub_username>/s4e-intern-devops:latest
docker login
docker push <dockerhub_username>/s4e-intern-devops:latest
helm install kod-uretici . --set image.repository=<dockerhub_username>/s4e-intern-devops,image.tag=latest
```

## File Structure

├── app.py

├── AI_assistant.py

├── requirements.txt

├── Dockerfile

├── .env

├── templates/

    └── index.html

├── chart/

    ├── Chart.yaml

    ├── values.yaml

└── templates/

       └── deployment.yaml

## Usage

Go to the web interface: http://localhost:5000 or IP of Minikube.

Enter a text in the Prompt field, for example:

"Write a Python class that sorts a list."

"Create a Python function that reads a file."

Click the Generate Code button.

View the generated title and code.

Copy the code to the clipboard with the Copy Code button

```bash
from s4e.config import *
from s4e.task import Task

class Job(Task):
    def run(self):
        asset = self.asset
        self.output['detail'] = sorted(asset)
        self.output['compact'] = self.output['detail']
        self.output['video'] = ["Sorting the list"]

    def calculate_score(self):
        self.score = self.param.get('max_score', 5)
```

### Repository name : onurcetin/s4e-intern-devops

### Interface : 
![image](https://github.com/user-attachments/assets/47ad5b56-4aa1-42df-9ce8-7151f5616a0f)

### Kubernetes : 

![kubernete](https://github.com/user-attachments/assets/829b24d7-e223-4ecd-b915-e1576de077e3)

### Heml deploy : 

![helm deploy](https://github.com/user-attachments/assets/2bead732-c9f9-4504-87b1-74ba77dad292)





