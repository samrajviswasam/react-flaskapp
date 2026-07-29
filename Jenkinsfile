pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/your-username/your-public-repo.git'
        BRANCH = 'main'

        IMAGE_NAME = 'react-flaskapp'
        IMAGE_TAG = 'latest'

        CONTAINER_NAME = 'myapp-container'
        HOST_PORT = '5000'
        CONTAINER_PORT = '80'
    }

    stages {

        stage('Clone Repository') {
            steps {
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                """
            }
        }

        stage('Stop Old Container') {
            steps {
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                """
            }
        }

        stage('Run Docker Container') {
            steps {
                sh """
                    docker run -d \
                    --name ${CONTAINER_NAME} \
                    -p ${HOST_PORT}:${CONTAINER_PORT} \
                    ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

        stage('Verify Container') {
            steps {
                sh """
                    docker ps
                """
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'Pipeline failed.'
        }

        always {
            sh 'docker images'
        }
    }
}
