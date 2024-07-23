"""Welcome to Reflex!."""

# Import all the pages.
from frontend.pages import *

import reflex as rx

# Definir un estado global para la autenticación
class AuthState(rx.State):
    authenticated: bool = False

    def login(self):
        self.authenticated = True

    def logout(self):
        self.authenticated = False

# Definir la página de inicio
def index():
    if AuthState.authenticated:
        return rx.box(
            rx.text("You are logged in!", color="green"),
            rx.button("Logout", on_click=AuthState.logout, color="red"),
        )
    else:
        return rx.box(
            rx.text("You are not logged in!", color="red"),
            rx.button("Login", on_click=AuthState.login, color="blue"),
        )

# Create the app.
app = rx.App(state = AuthState)
