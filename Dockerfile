FROM python

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY bot.py base.py .

ENTRYPOINT ["python", "bot.py"]