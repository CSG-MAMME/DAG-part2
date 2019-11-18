#!/bin/bash
# You should first import the key using gpg2 --import
# Maybe share key fingerprint? How can we verify?
gpg2 \
    --output ./Team_Bearland_Sheet1.pdf.gpg \
    --encrypt --recipient julian.pfeifle@upc.edu \
    ./Team_Bearland_Sheet1.pdf
