import os

from loe_simp_app_fw.config import Config
from loe_simp_app_fw.logger import Logger

Config("config.yaml", example_config_path="config-example.yaml", project_root_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
Logger("log", project_root_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

