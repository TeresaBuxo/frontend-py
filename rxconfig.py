import reflex as rx
from webapp.backend.config import constants as cs

URL_DATABASE = f'mysql+pymysql://{cs.USER}:{cs.PASSWORD}@{cs.HOST}:{cs.PORT}/{cs.SCHEMA}'

config = rx.Config(
    app_name="webapp",
    stylesheets=[
        "/fonts/ArialRoundedMTBold/arial_rounded.css",  # This path is relative to assets/
    ],
    # style = {
    #     "font_family": "Arial Rounded",
    #     "font_size": "16px",
    # },
    db_url = URL_DATABASE,
    frontend_port=3000,
    deploy_url='http://localhost:3000',
    api_url = "http://localhost:8000"
)