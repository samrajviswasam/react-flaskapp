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

                dir('frontend') {

                    sh 'npm install'

                }

            }

        }



        stage('Build React Application') {

            steps {

                dir('frontend') {

                    sh 'npm run build'

                }

            }

        }



        stage('Install Flask Dependencies') {

            steps {

                dir('backend') {

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

                dir('backend') {

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
