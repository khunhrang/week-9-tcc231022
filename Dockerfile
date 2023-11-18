# Base build
FROM python:3.10-alpine as base

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt

# Now multistage build
FROM python:3.10-alpine
WORKDIR app
COPY --from=base /usr/local/lib/python3.10/site-packages/ /usr/local/lib/python3.10/site-packages/
COPY --from=base /usr/local/bin/ /usr/local/bin/
COPY . .
EXPOSE 8000
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8000"]