pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'master',
                    url: 'https://github.com/samrajviswasam/myapp.git'
            }
        }

        stage('Install React Dependencies') {
            steps {
                dir('react-app') {
                    sh '''
                        npm install
                    '''
                }
            }
        }

        stage('Build React Application') {
            steps {
                dir('react-app') {
                    sh '''
                        npm run build
                    '''
                }
            }
        }

        stage('Install Flask Dependencies') {
            steps {
                dir('flaskapp') {
                    sh '''
                        python3 -m venv venv
                        venv/bin/pip install --upgrade pip
                        venv/bin/pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Stop Old Flask Server') {
            steps {
                sh '''
                    pkill -f gunicorn || true
                '''
            }
        }

        stage('Start Flask Backend') {
            steps {
                dir('flaskapp') {
                    sh '''
                        nohup venv/bin/gunicorn \
                        --bind 0.0.0.0:8000 \
                        app:app \
                        > gunicorn.log 2>&1 &
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                    sleep 5
                    curl http://localhost:8000 || true
                '''
            }
        }
    }

    post {
        success {
            echo "======================================="
            echo "Deployment Successful"
            echo "React Build Completed"
            echo "Flask Backend Running on Port 8000"
            echo "======================================="
        }

        failure {
            echo "======================================="
            echo "Deployment Failed"
            echo "Check the Jenkins Console Output"
            echo "======================================="
        }
    }
}
