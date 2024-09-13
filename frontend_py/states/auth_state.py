"""The authentication state."""
import reflex as rx
import httpx
from starlette.responses import Response
from ..constants import urls

class AuthState(rx.State):
    email: str = ""
    password: str = ""
    auth_response: str = ""
    login_error: bool = False
    signup_error: bool = False
    unexpected_error: bool = False

    def set_username(self, value: str):
        self.email = value

    def set_password(self, value: str):
        self.password = value

    async def handle_login(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://localhost:8000/api/users/token",
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
                    print(f"Login successful! Token: {self.token}")
                
                # Redirect or update UI after login
                    return rx.redirect(urls.PLATFORM_URL)

                else:
                    self.login_error = True
            else:
                self.login_error = True
        
        except Exception as err:
            self.unexpected_error=True

    async def handle_signup(self):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    "http://localhost:8000/api/users/create_user",
                    json={
                        "email": self.email,
                        "password": self.password,
                    },
                )
            
            if response.status_code == 200:
                response_data = response.json()
                return rx.redirect(urls.LOGIN_URL)

            elif response.status_code == 400:
                self.signup_error = True
            else:
                self.unexpected_error = True
        
        except Exception as err:
            self.unexpected_error = True