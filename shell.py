import asyncio

from dataclasses import dataclass
from typing import Optional

@dataclass
class RunOnShell:
    cmd: str
    stdout: str
    stderr: str
    return_code: Optional[int]

async def run(cmd: str):

    print(f"executing '{cmd}'")

    proc = await asyncio.create_subprocess_shell(
        cmd,
        stderr=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    print(f'[{cmd} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

    ros = RunOnShell(
        cmd=cmd,
        stdout=stdout.decode().strip(),
        stderr=stderr.decode().strip(),
        return_code=proc.returncode
    )

    return ros
