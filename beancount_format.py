import click
from pathlib import Path
from beancount.scripts.format import align_beancount


@click.command()
@click.argument(
    "filename",
    type=click.Path(exists=True, dir_okay=False, path_type=Path),
    nargs=-1,
)
@click.option("--prefix-width", "-w", type=int, help="Force fixed prefix width.")
@click.option("--num-width", "-W", type=int, help="Force fixed numbers width.")
@click.option(
    "--currency-column", "-c", type=int, help="Align curreencies to this column."
)
def main(filename, prefix_width, num_width, currency_column):
    """Modified version beancount.scripts.format.main

    Allows multiple filenames and overwrites each file
    """
    for filename in filename:
        with filename.open("r") as f:
            contents = f.read()
        formatted_contents = align_beancount(
            contents, prefix_width, num_width, currency_column
        )
        with filename.open("w") as f:
            f.write(formatted_contents)


if __name__ == "__main__":
    main()
