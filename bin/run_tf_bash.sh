#!/bin/bash -e
THISDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
source ${THISDIR}/project_envvars.sh
pushd ${DOCKER_DIR}
docker run \
    -it \
    -v ${PROJECTHOME_DIR}:${PROJECTHOME_DIR} \
    -v ${PROJECTHOME_DIR}/.keras:${PROJECTHOME_DIR}/.keras \
    -v ${PROJECTHOME_DIR}/.sklearndata:/scikit_learn_data \
    -w ${PROJECTHOME_DIR} \
    -u $(id -u):$(id -g) \
    ${TF_INTRO_IMAGE_TAG} \
    bash
