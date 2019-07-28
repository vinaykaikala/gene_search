docker login --username $DOCKER_USER --password $DOCKER_PASS
if [ "$TRAVIS_BRANCH" = "master" ]; then
TAG="latest"
else
TAG="$TRAVIS_BRANCH"
fi
docker build -f docker/Dockerfile -t genequery:latest .
docker tag genequery $DOCKER_REPO
docker push $DOCKER_REPO
