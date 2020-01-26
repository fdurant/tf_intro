#!/bin/bash -e
THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source ${THISDIR}/project_envvars.sh
pushd ${DOCKER_DIR}
docker build \
    --tag ${TF_INTRO_IMAGE_TAG} \
    ${DOCKER_DIR}
