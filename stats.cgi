#!/bin/bash

echo "<pre>$(sensors)</pre>"
echo "<pre>$(nvidia-smi -q -d temperature)</pre>"
