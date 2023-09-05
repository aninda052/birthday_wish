#!/bin/bash

celery -A birthday_wish worker -l info --concurrency 4