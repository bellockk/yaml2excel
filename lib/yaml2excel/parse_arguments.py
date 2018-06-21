import argparse

__version__ = '1.0.0'


def parse_arguments(args):
    """
    Define Program Options
    """
    PARSER = argparse.ArgumentParser(
        description='convert tables to/from yaml/excel', prog='convert')
    PARSER.add_argument('-V', '--version', action='version',
                        version='sut v{0}'.format(__version__))
    GROUP = PARSER.add_mutually_exclusive_group()
    GROUP.add_argument('-v', '--verbose', dest='log_level',
                       default='INFO',
                       action='store_const',
                       const='DEBUG',
                       help='increase output verbosity')
    GROUP.add_argument('-q', '--quiet', dest='log_level',
                       default='INFO',
                       action='store_const',
                       const='CRITICAL',
                       help='silence all but critical messages')
    GROUP.add_argument('-l', '--log-level', dest='log_level',
                       default='INFO',
                       choices=['DEBUG', 'INFO', 'WARNING', 'ERROR',
                                'CRITICAL'],
                       help='set logging level')
    GROUP = PARSER.add_mutually_exclusive_group()
    GROUP.add_argument('-e', '--to-excel', action='store_true')
    GROUP.add_argument('-y', '--to-yaml', dest='to_excel',
                       action='store_false')
    PARSER.add_argument('-o', '--output-path')
    PARSER.add_argument('-i', '--input-path')
    return PARSER.parse_args()
