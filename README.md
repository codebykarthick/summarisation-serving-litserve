# Serving Model Using LitServe
The blog post that explains the project in detail can be found [here.]()

## Introduction
This project tries to use LitServe library to load model from weights obtained during fine-tuning [here.](https://github.com/codebykarthick/summarisation-fine-tuning) It also tries to dockerise the solution through a `Dockerfile` which will allow us to publish the image and deploy it in any suitable environment to serve easily.

## Setup
Install the requirements listed in `requirements.txt` using the below command (preferably in a fresh venv or conda environment)

```bash
pip install -r requirements.txt
```

## Execution
The below command is a quick way to check the execution.

```bash
python -m app.main --port 8080 --batch 1
```

## Sample Request

Once the server is running locally (e.g., via `python main.py` or inside Docker), you can test it using any REST client like *Postman*, *VS Code HTTP Client*, or *Insomnia*. Here's a sample cURL command:

```bash
curl -X POST http://127.0.0.1:8080/predict \ 
     -H "Content-Type: application/json" \ 
     -d '{"input": "In the heart of a bustling city, a small community garden has become a sanctuary for people of all ages and backgrounds. Initially started as a weekend project by a retired schoolteacher, the garden quickly attracted attention from neighbors who were looking for a way to reconnect with nature and each other. Over time, raised beds filled with herbs, vegetables, and flowers transformed the once-abandoned lot into a vibrant green space. Children learned how to plant seeds and water responsibly, while seniors shared gardening tips and stories from their youth. Volunteers painted murals on the surrounding walls, depicting scenes of unity, growth, and biodiversity. As the seasons changed, so did the garden’s colors and rhythms. In spring, tulips and daffodils danced in the breeze; in summer, tomatoes ripened on the vine under the warmth of the sun. Autumn brought the crunch of fallen leaves, and winter blankets made everything quiet but not forgotten. The garden also became a hub for local events—storytelling evenings and cultural food tastings."}'
```

This will return a JSON response with the generated summary.

```json
{"output": "the generated summary"}
```