import requests
from typing import Dict, Any

from application.modules.http.IHttpClient import IHttpClient

class HttpClient(IHttpClient):
    
    @staticmethod
    async def get(url: str, params: Dict[str, Any] = None) -> requests.Response:
        response = requests.get(url, params = params)
        return response
    
    @staticmethod
    async def post(url: str, data: Dict[str, Any] = None, json: Dict[str, Any] = None) -> requests.Response:
        response = requests.post(url, data = data, json = json)
        return response
    
    @staticmethod
    async def put(url: str, data: Dict[str, Any] = None) -> requests.Response:
        response = requests.put(url, data = data)
        return response
    
    @staticmethod
    async def delete(url: str) -> requests.Response:
        response = requests.delete(url)
        return response
