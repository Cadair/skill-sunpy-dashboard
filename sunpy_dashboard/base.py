"""
Base types for representing data.
"""
from datetime import datetime
from typing import List, Optional

from pydantic.dataclasses import dataclass


async def get_pypi_version_time(session, name):
    url = f"https://pypi.org/pypi/{name}/json"

    async with session.get(url) as resp:
        info = (await resp.json())
    version = info["info"]["version"]
    time = datetime.fromisoformat(info["releases"][version][0]["upload_time"])
    return version, time


@dataclass
class Package():
    """
    Metadata about a package.
    """
    name: str
    version: str
    last_release: datetime
    logo: Optional[str] = None


@dataclass
class Job():
    """
    Information about a single CI job.
    """
    name: str
    status: str


@dataclass
class Build():
    """
    A single CI run.
    """
    url: str
    status: str
    time: datetime
    jobs: List[Job]