from argparse import ArgumentParser, Namespace
from typing import Any

from app.utils.constants import Constants


def create_arg_parser() -> ArgumentParser:
    parser = ArgumentParser()

    parser.add_argument('--batch', '-b', type=int, default=1,
                        help="The maximum number of requests to batch to run inference with the same model.")
    parser.add_argument('--port', '-p', type=int, default=8080,
                        help="Specify the port for the server to listen for incoming requests to.")

    return parser


def create_config(args: Namespace) -> dict[str, Any]:
    config = {}

    config[Constants.BATCH] = args.batch
    config[Constants.PORT] = args.port

    return config
