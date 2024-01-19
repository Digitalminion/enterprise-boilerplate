#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
________  .__       .__  __         .__      _____  .__       .__               
\______ \ |__| ____ |__|/  |______  |  |    /     \ |__| ____ |__| ____   ____  
 |    |  \|  |/ ___\|  \   __\__  \ |  |   /  \ /  \|  |/    \|  |/  _ \ /    \ 
 |    `   \  / /_/  >  ||  |  / __ \|  |__/    Y    \  |   |  \  (  <_> )   |  \
/_______  /__\___  /|__||__| (____  /____/\____|__  /__|___|  /__|\____/|___|  /
        \/  /_____/               \/              \/        \/               \/ 

_____     _                   _            _____     _ _             _     _       
|   __|___| |_ ___ ___ ___ ___|_|___ ___   | __  |___|_| |___ ___ ___| |___| |_ ___ 
|   __|   |  _| -_|  _| . |  _| |_ -| -_|  | __ -| . | | | -_|  _| . | | .'|  _| -_|
|_____|_|_|_| |___|_| |  _|_| |_|___|___|  |_____|___|_|_|___|_| |  _|_|__,|_| |___|
                      |_|                                        |_|           

An extensible project framework for quickly building enterprise compliant python projects

Copyright 2023 Digital Minion Llc

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
'''
__version__ = '0.0.1'
__author__ = 'DigitalMinion'
__email__ = 'overmind@digitalminion.com'

import argparse
from loguru import logger
import json

class Main:
    def __init__(self):
        with open("./config.json", "r") as config_file:
            config = json.load(config_file)
        # Extract logging configuration
            self.projects = config.get("projects",{})
            self.default_project_name = config.get('defaultProject',{})
            self.default_project = self.projects.get(self.default_project_name,{})
            self.log_config = self.default_project.get("logging", {})
            logger.configure(**self.log_config)
        # Configure loguru using the extracted logging configuration
        self.log = logger
        self.log.debug("Logging configured")
        # Create the main argparse object
        self.parser = argparse.ArgumentParser(description='Main parser for the program')
        
        # Add root arguments common across all projects
        self.parser.add_argument('--main_arg', type=str, help='Main argument for the program')
        # Parse the command-line arguments
        self.args = self.parser.parse_args()

        # Import the module dynamically and primary class dynamically
        module = __import__(self.default_project.get('entryModule',{}),fromlist=["Main"])
        project_class = getattr(module, 'Main')
        # # Initialize the entry class pass in our instance of arg parse
        self.project_instance = project_class(self.args, self.log)

    def start(self):
        # Use the argparse object to access main arguments)

        # Call sub-module processors
        self.project_instance.start()
        self.log.debug("end of framework application")

if __name__ == "__main__":
    main = Main()
    main.start()