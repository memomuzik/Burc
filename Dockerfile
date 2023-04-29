COPY ./app
RUN pip install -r python-telegram-bot
RUN pip install -r requests
RUN pip install -r requirments.txt
RUN mkdir /app/
WORKDIR /app/
CMD ["python3", "burc.py"
