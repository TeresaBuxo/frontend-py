import reflex as rx
import httpx
from starlette.responses import Response
from ..constants import urls
from typing import List, Dict 
from .auth_state import AuthState

class OrgState(AuthState):
    orgs: List[Dict[str, str]] = []

    async def get_my_orgs(self):

        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{urls.API_URL}api/orgs/organizations/",
                headers = {"Authorization": f"Bearer {self.token}"}
            )
        
        if response.status_code == 200:
            self.orgs = response.json()
            return self.orgs
        else:
            print(f"Failed to get orgs: {response.status_code}, {response.text}")
