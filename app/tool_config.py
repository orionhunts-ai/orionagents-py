"""
Configuring the environment for running ML flows against it.    
"""
from typing import List, Union, Dict 
    
class OrionAgentInit:
    def __init__(self, config_file):
        self.config = config_file
        
    def parse_config(self, config_file) -> List[str]:
        """Parses differently depending on the contents of the file"""
        return config_file #@TODO Add logic
    
    def service_login(self, kwargs**) -> List[str]:
        """Login to the service"""
        return kwargs
    
    
    
    