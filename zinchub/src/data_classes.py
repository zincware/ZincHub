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


@dataclass
class DataHub:
    """
    Data class to define the DataHub folder.
    """
    url: str
    format: str
    results: bool = False
    description: str = ""
    multi: bool = False


@dataclass
class MDSuiteCI(DataHub):
    """
    Dataclass for the MDSuite CI data.
    """
    url =
