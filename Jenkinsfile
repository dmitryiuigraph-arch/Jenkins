pipeline {
    agent any

    parameters {
        choice(
            name: 'ENV',
            choices: ['dev', 'prod'],
            description: 'Choose deployment environment'
        )
    }

    stages {

        stage('Deploy Message') {
            steps {
                echo "Deploying to ${params.ENV}"
            }
        }

        stage('Deploy Application') {
            steps {
                sshPublisher(
                    publishers: [
                        sshPublisherDesc(
                            configName: 'RemoteServer',
                            transfers: [
                                sshTransfer(
                                    sourceFiles: '**/*',
                                    removePrefix: '',
                                    remoteDirectory: "/opt/app/${params.ENV}",
                                    execCommand: 'echo Deployment completed'
                                )
                            ],
                            verbose: true
                        )
                    ]
                )
            }
        }
    }

    post {
        always {
            deleteDir()
        }
    }
}
