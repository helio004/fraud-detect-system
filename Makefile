MODEL_PATH := $(shell pwd)/model
PIPELINE_IMAGE := catboost_airflow
API_IMAGE := catboost_airflow

.PHONY: deploy destroy write_env

run-pipeline:
	docker build -t $(PIPELINE_IMAGE) pipeline -f pipeline/Dockerfile
	docker run -d -p 8080:8080 -v ${MODEL_PATH}:/app/model $(PIPELINE_IMAGE)

run-api:
	docker build -t $(API_IMAGE) app -f app/Dockerfile
	docker run -d -p 8000:8000 -v ${MODEL_PATH}:/app/model $(API_IMAGE)

clean-env:
	docker rm -f $(shell docker ps -a -q)
	docker rmi -f $(shell docker images -a -q)
	sudo rm -r $(MODEL_PATH)
