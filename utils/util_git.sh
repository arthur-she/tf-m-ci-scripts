#!/usr/bin/env bash
#
# Copyright (c) 2025 Arm Limited. All rights reserved.
#
# SPDX-License-Identifier: BSD-3-Clause
#

# Don't print mouthful "You are in 'detached HEAD' state." messages.
git config --global advice.detachedHead false

# Global defaults
GIT_CLONE_PARAMS="--no-checkout"

function git_clone() {
    # Parse the repo elements
    local REPO_URL=$1
    local REPO_PATH=$2
    local REPO_REFSPEC=$3
    local REPO_SYNC_CMD=$4

    # In case repository is not defined, just skip it
    if [ -z "${REPO_URL}" ]; then
        return
    fi

    # Clone if it does not exit
    if [ ! -d ${REPO_PATH} ]; then
                # Shallow clone the repo without checkout
        git clone --quiet ${GIT_CLONE_PARAMS} "${REPO_URL}" "${REPO_PATH}"

        # If a refspec or commit SHA was provided, fetch & checkout shallowly
        if [ -n "${REPO_REFSPEC}" ]; then
            git -C "${REPO_PATH}" fetch --quiet --depth=1 origin "${REPO_REFSPEC}" \
                || git -C "${REPO_PATH}" fetch --quiet --all --depth=1

            git -C "${REPO_PATH}" checkout --quiet FETCH_HEAD 2>/dev/null \
                || git -C "${REPO_PATH}" checkout --quiet "${REPO_REFSPEC}"
        fi

        # If requested, shallow-init and update all submodules
        if [ "${REPO_SYNC_CMD}" = "SYNC_ALL_SUBMODULES" ]; then
            git -C "${REPO_PATH}" submodule update --init --recursive --depth=1 --quiet
        fi

        echo -e "Share Folder ${REPO_PATH} $(git -C "${REPO_PATH}" rev-parse --short HEAD)\n"

    fi
}
