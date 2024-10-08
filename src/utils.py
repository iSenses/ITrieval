import click
import httpx
from httpx._transports.default import ResponseStream
import json
import textwrap
from typing import List, Dict, Iterator

class _LoggingStream(ResponseStream):
    def __iter__(self) -> Iterator[bytes]:
        for chunk in super().__iter__():
            click.echo(f"    {chunk.decode()}", err=True)
            yield chunk


def _no_accept_encoding(request: httpx.Request):
    request.headers.pop("accept-encoding", None)


def _log_response(response: httpx.Response):
    request = response.request
    click.echo(f"Request: {request.method} {request.url}", err=True)
    click.echo("  Headers:", err=True)
    for key, value in request.headers.items():
        if key.lower() == "authorization":
            value = "[...]"
        if key.lower() == "cookie":
            value = value.split("=")[0] + "=..."
        click.echo(f"    {key}: {value}", err=True)
    click.echo("  Body:", err=True)
    try:
        request_body = json.loads(request.content)
        click.echo(
            textwrap.indent(json.dumps(request_body, indent=2), "    "), err=True
        )
    except json.JSONDecodeError:
        click.echo(textwrap.indent(request.content.decode(), "    "), err=True)
    click.echo(f"Response: status_code={response.status_code}", err=True)
    click.echo("  Headers:", err=True)
    for key, value in response.headers.items():
        if key.lower() == "set-cookie":
            value = value.split("=")[0] + "=..."
        click.echo(f"    {key}: {value}", err=True)
    click.echo("  Body:", err=True)
    response.stream._stream = _LoggingStream(response.stream._stream)  # type: ignore

def client_with_logging() -> httpx.Client:
    return httpx.Client(
        event_hooks={"request": [_no_accept_encoding], "response": [_log_response]}
    )
