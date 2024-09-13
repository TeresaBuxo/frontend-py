import reflex as rx
import httpx
from starlette.responses import Response
from ..constants import urls
from typing import List, Dict 

class ProjectState(rx.State):
    projects: List[Dict[str, str]] = []

    async def get_list_projects(self):

        async with httpx.AsyncClient() as client:
            response = await client.get(
                "http://localhost:8000/api/projects/",
            )
        
        if response.status_code == 200:
            self.projects = response.json()


    
