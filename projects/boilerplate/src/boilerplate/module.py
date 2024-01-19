class Main:
    def __init__(self, args, log):
        self.log = log
        self.log.debug('loading submodule')
        self.args = args
        # You can create a sub-parser specific to this module if needed
        # local_parser = self.args.subparsers.add_parser('boilerplate')
        # local__parser.add_argument('--example', type=str, help='Argument for Boilerplate Module')
        # local__args = local__parser.parse_args()
        self.log.debug('submodule loaded')

    def start(self):
        self.log.debug("submodule ran")