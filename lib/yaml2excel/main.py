import sys
import logging
from yaml2excel import yaml2excel
from excel2yaml import excel2yaml
from parse_arguments import parse_arguments
from parse_arguments import __version__


def main(args):
    if args.to_excel:
        yaml2excel(args.output_path, args.input_path)
    else:
        excel2yaml(args.output_path, args.input_path)


if __name__ == "__main__":

    # Parse Arguments
    ARGS = parse_arguments(sys.argv[1:])

    # Setup Logging
    logging.basicConfig(level=getattr(logging, ARGS.log_level),
                        format='%(message)s')

    # Log Header
    logging.info('YAML/Excel Converter v%s', __version__)
    logging.info('  Input: %s' % ARGS.input_path)
    logging.info('  Output: %s' % ARGS.output_path)

    # Write Output
    main(ARGS)

    # Log Footer
    logging.info('Conversion completed successfully')
