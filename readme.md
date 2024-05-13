# Projectile motion

This project uses [Django](https://www.djangoproject.com/) and [Docker](https://www.docker.com/) to display a simulation of the inclined throw with friction in a web application.

## Prerequisites
- [Python](https://www.python.org/)
- [Docker](https://docs.docker.com/engine/install/)

## Setup
- `git clone https://github.com/51moon/projectile_motion.git`
- `cd projectile_motion`
- `python -m venv .venv`
- `source .venv/bin/activate`
- `docker build -t projectile_motion .`
- `docker run -it -p 8000:8000 projectile_motion`

Now you can start the development server at http://0.0.0.0:8000.

## Preview
<img src="screenshot.png" width="600">