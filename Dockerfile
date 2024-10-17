FROM python:3.11-slim-buster

# Install dependencies
COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy app code to container
COPY app.py /app/

# Set working directory
WORKDIR /app

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py"]