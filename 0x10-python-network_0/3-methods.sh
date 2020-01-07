#!/bin/bash
# This script displays the HTTP methods allowed by the server
curl -Is "$1" | grep Allow | cut -d ":" -f 2
