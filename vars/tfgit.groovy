/*
 * Copyright (c) 2024, Arm Limited. All rights reserved.
 *
 * SPDX-License-Identifier: BSD-3-Clause
 *
 */

def checkout_ci_scripts() {
    checkout([
        $class: 'GitSCM',
        branches: [[name: '$CI_SCRIPTS_BRANCH']],
        userRemoteConfigs: [[
            credentialsId: 'GIT_SSH_KEY',
            url: '$CI_SCRIPTS_REPO',
            refspec: '+refs/heads/*:refs/remotes/origin/* +refs/changes/*:refs/remotes/origin/refs/changes/*'
        ]]
    ])
}
