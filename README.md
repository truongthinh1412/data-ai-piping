# data-ai-piping

docker compose up -d to run mongo (can integrate both servers to docker compose later)

create a conda environment and install requirements.txt to install dependencies

run fastapi dev mock_server.py --port 8002 in the conda env to run the mock server

run fastapi dev server.py --port 8001 in the conda env to run the main server

run fastapi dev save_large_file_server.py --port 8003 in the conda env to run the upload server

run python test.py to run test

For the choice between amazon S3 and mongodb gridfs I would choose the gridfs due to the fact that we will need to query this data along with other data in the mongodb database, which will be much easier. The amazon S3 would also be a good choice if we do decide to be very scalable and storing massive amount of data, requiring to access this data in differents location in the world. But it seems this is not our current priorities.

