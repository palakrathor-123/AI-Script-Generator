import requests

def generate_script(topic, tone, options=None):

    prompt = f"""
    Write a short {tone} script about {topic}.
    Extra instructions: {options}
    Keep response under 50 words.
    """

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "phi3:mini",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return data.get("response", "No response from AI")