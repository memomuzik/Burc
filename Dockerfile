COPY ./app
RUN pip install  python-telegram-bot
RUN pip install  requests
RUN pip install  requirments.txt
RUN mkdir /app/
WORKDIR /app/
CMD ["python3", "burc.py"]
