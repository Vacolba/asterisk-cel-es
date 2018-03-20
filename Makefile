all: push

TAG = 0.0.2
PREFIX = vacolba/asterisk-cel-es

container:
	docker build -t $(PREFIX):$(TAG) .

push: container
	docker push $(PREFIX):$(TAG)

clean:
	docker rmi -f $(PREFIX):$(TAG) || true
