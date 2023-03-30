# Copyright 2023 The Wordcab Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Configuration module of the Wordcab ASR API."""

from os import getenv
from dotenv import load_dotenv

from pydantic import BaseSettings


class Settings(BaseSettings):
    project_name: str
    version: str
    description: str
    api_prefix: str
    debug: bool
    batch_size: int
    max_wait: float
    


load_dotenv()

settings = Settings(
    project_name=getenv("PROJECT_NAME"),
    version=getenv("VERSION"),
    description=getenv("DESCRIPTION"),
    api_prefix=getenv("API_PREFIX"),
    debug=getenv("DEBUG"),
    batch_size=getenv("BATCH_SIZE"),
    max_wait=getenv("MAX_WAIT"),
)