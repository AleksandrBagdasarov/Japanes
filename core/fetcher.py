import httpx
from httpx import Response
import asyncio

from .config import DEFAULT_RETRIES, DEFAULT_TIMEOUT, PROXIES
from .logger import logger


async def request(method: str,
                     url: str,
                     allow_status_codes: list = [200],
                     retries: int = DEFAULT_RETRIES,
                     proxies: str = PROXIES,
                     timeout: str = DEFAULT_TIMEOUT,
                     **kwargs) -> Response:

    for _ in range(retries + 1):
    
        if proxies:
            async with httpx.AsyncClient(verify=False, timeout=timeout) as client:
                response = await client.request(method, url, **kwargs)
        else:
            async with httpx.AsyncClient(proxies=proxies, verify=False, timeout=timeout) as client:
                response = await client.request(method, url, **kwargs)
                

        try:
            assert response.status_code in allow_status_codes
            logger.debug(f'{response.status_code} - {response.url}')
            return response

        except AssertionError:
            logger.exception(f'{response.status_code} - {response.url}')
            await asyncio.sleep(3)


# asyncio.run(request('GET', 'https://pypi.org/project/httpx/'))