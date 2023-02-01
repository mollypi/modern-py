"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Modern Py."""


if __name__ == "__main__":
    main(prog_name="modern-py")  # pragma: no cover
