#!/bin/bash

# Copyright 2018 Marc René Schädler
#
# This file is part of the mobile hearing aid prototype project
# The the mobile hearing aid prototype project is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# The mobile hearing aid prototype project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with the mobile hearing aid prototype project. If not, see http://www.gnu.org/licenses/.


echo "killall thresholdnoise"
killall thresholdnoise -9 &> /dev/null

echo "killall pink noise"
killall pinknoise -9 &> /dev/null

echo "killall abhang"
killall abhang -9 &> /dev/null

echo "killall mha"
killall mha -9 &> /dev/null

echo "killall jackd"
killall jackd -9 &> /dev/null

echo "killall commander.sh"
killall commander.sh -9 &> /dev/null

echo "killall python (HHYL2H)"
killall python3.5

