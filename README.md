# pjecz-plataforma-web-api

API de la Plataforma Web del PJECZ.

Arrancar

    uvicorn --host=0.0.0.0 api.app:app --reload

Arrancar con gunicorn

    gunicorn -w 4 -k uvicorn.workers.UvicornWorker api.app:app
