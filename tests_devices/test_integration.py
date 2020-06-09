# Copyright 2018-2020 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests that plugin devices are accessible and integrate with PennyLane"""
import numpy as np
import pennylane as qml
import pytest

from conftest import all_devices

print(all_devices)

class TestDeviceIntegration:
    """Test the devices work correctly from the PennyLane frontend."""

    @pytest.mark.parametrize("d", all_devices)
    def test_load_device(self, d):
        """Test that the device loads correctly"""

        dev = qml.device(d, wires=2, shots=1024)
        assert dev.num_wires == 2
        assert dev.shots == 1024
        assert dev.short_name == d
