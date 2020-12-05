from src.modeling.config import Config

import logging
import os
import click

logger = logging.getLogger(__name__)
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)

"""Main script for running experiments"""


@click.command()
@click.argument("train_data_path")
@click.argument("test_data_path")
@click.argument("config_fn")
@click.option("--train_mode", is_flag=True)
@click.option("--pred_mode", is_flag=True)
def main(train_data_path, test_data_path, config_fn, train_mode, pred_mode):
    config = Config.read(config_fn)
    logger.info(f"Running experiment with Config: {config}")
    # TODO
    pass


if __name__=='__main__':
    main()
