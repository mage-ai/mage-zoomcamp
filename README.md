## Data Engineering Zoomcamp - Week 2

Welcome to Mage! Mage is an open-source, hybrid framework for transforming and integrating data. ✨

In this module, you'll learn how to use the Mage platform to author and share _magical_ data pipelines. This will all be covered in the course, but if you'd like to learn a bit more about Mage, check out our docs [here](https://docs.mage.ai/introduction/overview). 

Here are some other helpful links for your journey:

- [Mage Slack](https://www.mage.ai/chat)
- [Mage's GitHub](https://github.com/mage-ai/mage-ai)

## Let's get started

This repo contains a Docker Compose template for getting started with a new Mage project. It requires Docker to be installed locally. If Docker is not installed, please follow the instructions [here](https://docs.docker.com/get-docker/). 

You can start by cloning the repo:

```bash
git clone https://github.com/mage-ai/data-engineering-zoomcamp.git mage-data-engineering-zoomcamp
```

Then, build the Docker image:

```bash
cd mage-data-engineering-zoomcamp
docker compose build
```

Finally, start the Docker container:

```bash
docker compose up
```

Now, navigate to http://localhost:6789 in your browser!

Voila! You're ready to get started with the course. 