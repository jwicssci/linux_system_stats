#!/bin/bash

echo "<pre>$(sensors)</pre>"
echo "<pre>$(sensors -j)</pre>"
echo "<pre>$(nvidia-smi -q -d temperature)</pre>"
echo "<pre>$(nvidia-smi -x -q | xq)</pre>"

