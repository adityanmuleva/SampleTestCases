pipeline {
    agent any

    environment {
        SONAR_SCANNER_HOME = tool 'SonarQube'        
        SONAR_TOKEN = credentials('sonar-token')      
        SONAR_URL = 'http://sonarqube:9000'           
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out the code...'
                checkout scm
            }
        }

        stage('Prerequisite') {
            steps {
                echo 'Setting up Python environment...'
                sh 'python3 -m venv venv'
            }
        }

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh './venv/bin/pytest --cov=src --cov-report=xml --cov-report=term'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Performing Code Analysis'
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    $SONAR_SCANNER_HOME/bin/sonar-scanner \
                      -Dsonar.host.url=$SONAR_URL \
                      -Dsonar.token=$SONAR_TOKEN
                    '''
                }
                echo 'Code Analysis Completed'
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
        always {
            echo 'Cleaning up workspace...'
            cleanWs()
        }
    }
}
