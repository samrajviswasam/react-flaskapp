pipeline {

    agent any


    stages {


        stage('Checkout Code') {

            steps {

                git 'https://github.com/samrajviswasam/myapp.git'

            }

        }



        stage('Install React Dependencies') {

            steps {

                dir('react-app') {

                    sh 'npm install'

                }

            }

        }



        stage('Build React Application') {

            steps {

                dir('react-app') {

                    sh 'npm run build'

                }

            }

        }



        stage('Install Flask Dependencies') {

            steps {

                dir('flaskapp') {

                    sh '''

                    python3 -m venv venv

                    . venv/bin/activate

                    pip install -r requirements.txt

                    '''

                }

            }

        }



        stage('Start Flask Backend') {

            steps {

                dir('flaskapp') {

                    sh '''

                    nohup python3 app.py &

                    '''

                }

            }

        }


    }


    post {

        success {

            echo 'Deployment Successful'

        }


        failure {

            echo 'Deployment Failed'

        }

    }

}
