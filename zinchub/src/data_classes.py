"""
ZincHub: A Zincwarecode package.

License
-------
This program and the accompanying materials are made available under the terms
of the Eclipse Public License v2.0 which accompanies this distribution, and is
available at https://www.eclipse.org/legal/epl-v20.html

SPDX-License-Identifier: EPL-2.0

Copyright Contributors to the zincwarecode Project.

Contact Information
-------------------
email: zincwarecode@gmail.com
github: https://github.com/zincware
web: https://zincwarecode.com/

Citation
--------
If you use this module please cite us with:

Summary
-------
"""
from dataclasses import dataclass
import yaml
from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from pathlib import Path


def github_to_raw(url):
    """Take a GitHub url and convert it to the url to access raw data"""
    return url.replace(
        "github.com", "raw.githubusercontent.com"
    ).replace(
        "/tree", ""
    )


@dataclass
class DataHub:
    """
    Data class to define the DataHub folder.
    """
    url: str
    info: dict = None
    file_compressed: str = None
    file_raw: str = None
    format: str = None
    results: bool = False
    description: str = ""
    multi: bool = False

    def __post_init__(self):
        """Get the information from the info file"""
        with urlopen(github_to_raw(self.url + "/info.yaml")) as url:
            yaml_content = url.read()

        self.info = yaml.safe_load(yaml_content)
        self.file_compressed = self.info['file']['compressed']
        self.file_raw = self.info['file']['raw']

    def get_file(self, path):
        """Download the file from the URL into path"""
        with urlopen(github_to_raw(self.url + "/" + self.file_compressed)) as url:
            with ZipFile(BytesIO(url.read())) as file:
                file.extract(self.file_raw, path=path)


if __name__ == '__main__':
    LiCl = DataHub(url="https://github.com/zincware/DataHub/tree/main/NaCl_gk_i_q")
