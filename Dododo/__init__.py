"""
akamai.edgegrid
~~~~~~~~~~~~~~~

This library provides an authentication handler for Requests that implements the 
Akamai {OPEN} EdgeGrid client authentication protocol as 
specified by https://developer.akamai.com/introduction/Client_Auth.html.
For more information visit https://developer.akamai.com.

usage:

    >>> import requests
    >>> from akamai.edgegrid import EdgeGridAuth
    >>> from urlparse import urljoin

    >>> baseurl = 'https://akaa-WWWWWWWWWWWW.luna.akamaiapis.net/'
    >>> s = requests.Session()
    >>> s.auth = EdgeGridAuth(
        client_token='akab-XXXXXXXXXXXXXXXXXXXXXXX',
        client_secret='YYYYYYYYYYYYYYYYYYYYYYYYYY',
        access_token='akab-ZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
    )

... now you have a requests session object that can be used to make {OPEN} requests

    >>> result = s.get(urljoin(baseurl, '/diagnostic-tools/v1/locations'))
    >>> result.status_code
    200
    >>> result.json()['locations'][0]
    Hongkong, Hong Kong
"""

from .edgegrid import EdgeGridAuth
from .edgerc import EdgeRc
__all__=['EdgeGridAuth', 'EdgeRc']

__title__ = 'GMRIGHT'
__version__ = '6.0.9'
__author__ = 'KENJA BITO'
__license__ = 'GMRIGHT'6.0.9'
__copyright__ = 'Copyright 2019 GMRIGHT Technologies'

# Copyright 2019 GMRIGHT Technologies, Inc. All Rights Reserved
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     *GMRIGHT* lecense
#  
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
