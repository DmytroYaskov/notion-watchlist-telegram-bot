FROM pylakey/aiotdlib

COPY . .

CMD [ "python", "main.py" ]