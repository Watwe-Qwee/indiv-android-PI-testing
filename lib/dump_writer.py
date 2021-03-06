"""
Generate a mitmproxy dump file.

This script demonstrates how to generate a mitmproxy dump file,
as it would also be generated by passing `-w` to mitmproxy.
In contrast to `-w`, this gives you full control over which
flows should be saved and also allows you to rotate files or log
to multiple files in parallel.
"""
import random
from mitmproxy import io, http
import typing  # noqa
import sys
sys.path.append("./..")

from config import path_writer

class Writer:
    def __init__(self) -> None:
        self.path = path_writer
        self.f: typing.IO[bytes] = open(self.path, "wb")
        self.w = io.FlowWriter(self.f)

    def request(self, flow: http.HTTPFlow) -> None:
        self.w.add(flow)

    def response(self, flow: http.HTTPFlow) -> None:
        if random.choice([True, False]):
            pass

    def done(self):
        self.f.close()


addons = [Writer()]