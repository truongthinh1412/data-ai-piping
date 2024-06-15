# data-ai-piping

docker compose up -d to run mongo (can integrate both servers to docker compose later)

create a conda environment and install requirements.txt to install dependencies

run fastapi dev mock_server.py --port 8002 in the conda env to run the mock server

run fastapi dev server.py --port 8001 in the conda env to run the main server

run python test.py to run test