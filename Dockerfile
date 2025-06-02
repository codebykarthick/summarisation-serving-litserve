FROM pytorch/pytorch:2.7.0-cuda12.8-cudnn9-runtime

# Create the server directory in the container and set it as the working directory
RUN mkdir -p /root/server
WORKDIR /root/server

# Copy application code and model files into the server directory
COPY app/ ./app/
COPY model/ ./model/

# Copy requirements and startup script into the server directory
COPY requirements.txt ./
COPY start.sh ./

# Install all Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the startup script is executable
RUN chmod +x start.sh

# Specify the startup script as the command to run when the container starts
CMD ["./start.sh"]