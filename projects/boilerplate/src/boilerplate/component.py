'''
Digital Minion - Enterprise Boilerplate
An extensible project framework for quickly building enterprise compliant python projects

Copyright 2024 Digital Minion Llc

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

            ********************************************************************************
            ********************************************************************************
            **                                                                            **
            **                          MAKE A COPY BEFORE EDITTING                       **
            **                                                                            **
            ** Make a copy of the folder containing this template file before editing it! **
            **                                                                            **
            **                          MAKE A COPY BEFORE EDITTING                       **
            **                                                                            **
            ********************************************************************************
            ********************************************************************************

boilerplate.component:
    implements:
        BoilerplateComponent

'''
class BoilerplateComponent:
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