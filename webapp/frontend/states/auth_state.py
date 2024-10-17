"""The authentication state."""
import reflex as rx
import httpx
from starlette.responses import Response
from ..constants import urls
from typing import Optional,Dict
import threading

class AuthState(rx.State):
    email: str = ""
    password: str = ""
    auth_response: str = ""
    token: Optional[str] = None
    is_authenticated: bool = False
    show_error: bool = False
    error_message:str = None

    def set_username(self, value: str):
        self.email = value

    def set_password(self, value: str):
        self.password = value

    # Function to show the callout and hide it after 5 seconds
    def show_error_message(self):
        self.show_error = True  # Show the callout
        # Use a timer to call hide_callout after 5 seconds
        threading.Timer(5.0, self.hide_callout).start()

    # Function to hide the callout
    def hide_callout(self):
        self.show_error = False
    
    async def handle_login(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{urls.API_URL}api/users/token",
                    data={
                        "username": self.email,
                        "password": self.password,
                    },
                    headers={"Content-Type": "application/x-www-form-urlencoded"},
                )
            
            if response.status_code == 200:
                response_data = response.json()
                access_token = response_data.get("access_token")

                if access_token:
                    self.token = access_token
                    self.is_authenticated = True
                    print(f"Login successful! Token: {self.token}")
                
                # Redirect or update UI after login
                    return rx.redirect(urls.PLATFORM_URL)

                else:
                    self.error_message = "Your email or password are invalid"
                    self.show_error_message()
            else:
                self.error_message = "Your email or password are invalid"
                self.show_error_message()
        
        except Exception as err:
            self.error_message = "There was an unexpected error"
            self.show_error_message()

    async def handle_signup(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{urls.API_URL}api/users/create_user",
                    json={
                        "email": self.email,
                        "password": self.password,
                    },
                )
            
            if response.status_code == 200:
                response_data = response.json()
                return rx.redirect(urls.LOGIN_URL)

            elif response.status_code == 400:
                self.error_message = "Email already registered. Please log in."
                self.show_error_message()
            else:
                self.error_message = "There was an unexpected error"
                self.show_error_message()
        
        except Exception as err:
            self.error_message = "There was an unexpected error"
            self.show_error_message()
        
    async def handle_logout(self):
        self.token = None
        self.is_authenticated = False
        return rx.redirect(urls.HOME_URL)
    
    # Check if the user is authenticated by verifying the token
    def check_auth(self):
        if self.token:
            # Optionally, add token validation logic here
            self.is_authenticated = True
        else:
            self.is_authenticated = False