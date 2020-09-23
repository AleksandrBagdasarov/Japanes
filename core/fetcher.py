import httpx
from httpx import Response

from .config import DEFAULT_RETRIES, DEFAULT_TIMEOUT, PROXIES
from .logger import logger

# class Fetcher:

#     @staticmethod
#     async def request(method,
#                       url,
#                       allow_status_codes: list = None,
#                       retries: int = DEFAULT_RETRIES,
#                       **kwargs) -> Response:
#         proxies = kwargs.pop('proxies', PROXIES)
#         timeout = kwargs.pop('timeout', DEFAULT_TIMEOUT)
#         for order in range(retries + 1):
#             try:
#                 async with httpx.AsyncClient(proxies=proxies, verify=False, timeout=timeout) as client:
#                     response = await client.request(method, url, **kwargs)
#                     if allow_status_codes:
#                         Fetcher.validate_response_status_codes(response, allow_status_codes)
#                 return response
#             except:
#                 logger.exception(f'{url=}')

#     @staticmethod
#     def validate_response_status_codes(request: Response, allow_status_codes: list):
#         assert request.status_code in allow_status_codes


async def request(method: str,
                     url: str,
                     allow_status_codes: list = [200],
                     retries: int = DEFAULT_RETRIES,
                     proxies: str = PROXIES,
                     timeout: str = DEFAULT_TIMEOUT,
                     **kwargs):
    _status_code = None
    for _ in range(retries + 1):
        try:
            async with httpx.AsyncClient(proxies=proxies, verify=False, timeout=timeout) as client:
                response = await client.request(method, url, **kwargs)
                _status_code = response.status_code
                assert response.status_code in allow_status_codes
            return response
        except:
            logger.exception(f'{_status_code} - {url}')

    