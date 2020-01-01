from typing import Dict

from mee6_py_api.config import API_BASE_URL, GUILD_ID
from mee6_py_api.constants import HTTP_STATUS_SUCCESS
from mee6_py_api.exceptions import HTTPRequestError, BadRequestError, UnauthorizedError, TooManyRequestsError
from pprint import pprint
import asyncio
import aiohttp

from mee6_py_api.plugins.levels import Levels
from mee6_py_api.utils.logging import BaseLoggingService

http_status_errors = dict([(400, BadRequestError),
                          (401, UnauthorizedError),
                          (429, TooManyRequestsError),
                          (500, HTTPRequestError),
                          ])

def get_http_exception_for_status(resp_status):
    if resp_status in http_status_errors:
        return http_status_errors[resp_status]
    else:
        return HTTPRequestError

def check_http_response_for_errors(response, resp_status, resp_headers):
    if resp_status != HTTP_STATUS_SUCCESS:
        raise get_http_exception_for_status(resp_status)("Received an unknown bad response from server. \n"
                                                       "response: {} \n"
                                                       "status: {} \n"
                                                       "header: {}"
                                                       .format(response, resp_status, resp_headers))


class API(BaseLoggingService):
    base_url = API_BASE_URL
    default_guild_id: int = None

    def __init__(self, guild_id = GUILD_ID):
        self.default_guild_id = guild_id

        # Attach plugins
        self.levels = Levels(self)

    #
    # Networking functionality
    #
    async def send_post_request_and_get_response(self, url, payload, headers=None,
                                                 check_response_for_errors=True) -> Dict:
        resp_headers = None
        resp_status = None
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(json=payload, url=url, headers=headers) as resp:
                    resp_headers = resp.headers
                    resp_status = resp.status
                    response = await resp.json()

        except Exception as e:
            raise get_http_exception_for_status(resp_status)("Received an unknown bad response from server. \n"
                                   "error: {} \n"
                                   "status: {} \n"
                                   "header: {}"
                                   .format(e, resp_status, resp_headers))

        if check_response_for_errors:
            check_http_response_for_errors(response, resp_status, resp_headers)

        return response

    async def send_get_request_and_get_response(self, url, params) -> Dict:
        resp_headers = None
        resp_status = None
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url, params=params) as resp:
                    resp_headers = resp.headers
                    resp_status = resp.status
                    response = await resp.json()

        except Exception as e:
            raise get_http_exception_for_status(resp_status)("Received an unknown bad response from server. \n"
                                                             "error: {} \n"
                                                             "status: {} \n"
                                                             "header: {}"
                                                             .format(e, resp_status, resp_headers))

        check_http_response_for_errors(response, resp_status, resp_headers)

        return response







