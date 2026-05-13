AI Script Generator
An AI-powered Script Generator built using FastAPI, HTML/CSS, and Ollama.
This project generates scripts instantly based on topic, tone, and user instructions.

Features
* AI Script Generation
* FastAPI Backend
* Ollama Local AI Integration
* Professional Dashboard UI
* Different Script Tones
* Real-Time Script Output
* Fast Response Generation
* 
Technologies Used
* Python
* FastAPI
* HTML
* CSS
* Jinja2 Templates
* Ollama
* Phi3 Mini Model
* 
Project Structure
Plain text
script-ai-generator/
│
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── ai_model.py
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── run.py
├── requirements.txt
└── README.md

Installation
* Clone the Repository
Bash
git clone <repository-link>

* Install Dependencies
Bash
pip install -r requirements.txt

* Install Ollama
Download and install Ollama from:
Ollama Official Website⁠�

* Download AI Model
Bash
ollama pull phi3:mini

* Run Ollama
Bash
ollama run phi3:mini

* Run the Project
Bash
python run.py

* Open in Browser
Plain text
http://127.0.0.1:8000

How It Works
1. User enters Topic, Tone, and Instructions.
2. FastAPI sends the prompt to Ollama.
3. Phi3 Mini AI model generates a script.
4. Result is displayed on the dashboard.
   
Example Inputs
* Topic
Plain text
How students can stay productive

* Tone
Plain text
Motivational

* Options
Plain text
Keep it short and simple.

Future Improvements
1. Copy Script Button
2. Download as PDF
3. Dark Mode UI
4. Voice Input
5. Multiple Language Support

 Dashboard Overview
 
Author
Palak Rathore
