COPY ./app
RUN pip install -r python-telegram-bot
RUN pip install -r requests
RUN pip install -r requirments.txt
