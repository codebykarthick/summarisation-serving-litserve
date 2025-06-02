# While this one line command can be directly given as the startup command to Docker container
# This allows for more flexibility such as loading secrets, etc to be passed along if the need
# arises.
python -m app.main --port 8080 --batch 16