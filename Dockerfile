FROM python:3
RUN pip install -U scikit-learn && pip install Flask
WORKDIR /app
COPY . /app 
EXPOSE 5000
CMD python app.py 
