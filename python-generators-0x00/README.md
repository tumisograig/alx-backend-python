# python-generators-0x00

## Overview
This project demonstrates how to use Python generators efficiently in backend systems involving SQL databases.

## Features
- Setup MySQL database with user data
- Stream records row-by-row
- Batch processing of large datasets
- Lazy pagination
- Memory-efficient average age calculation

## Files
- `seed.py`: Sets up and seeds MySQL database
- `0-stream_users.py`: Streams rows one-by-one
- `1-batch_processing.py`: Streams data in batches and filters
- `2-lazy_paginate.py`: Paginates data lazily
- `4-stream_ages.py`: Calculates average age using generators
