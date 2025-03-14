pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('sonar-token')      
        SONAR_URL = 'http://sonarqube:9000'           
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    try {
                        echo 'Checking out the code...'
                        checkout scm  
                    } catch (Exception e) {
                        error "Checkout stage failed: ${e.message}"
                    }
                }
            }
        }

        stage('Prerequisite') {
            steps {
                script {
                    try {
                        echo 'Setting up Python environment...'
                        sh 'cd "$WORKSPACE" || exit 1'
                        sh 'python3 -m venv venv'  
                    } catch (Exception e) {
                        error "Prerequisite stage failed: ${e.message}"
                    }
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    try {
                        echo 'Installing dependencies...'
                        sh './venv/bin/pip install --upgrade pip'
                        sh './venv/bin/pip install -r requirements.txt'
                    } catch (Exception e) {
                        error "Build stage failed: ${e.message}"
                    }
                }
            }
        }

        stage('Test') {
            steps {
                script {
                        echo 'Running tests...'
                        sh './venv/bin/pytest --cov=src --cov-report=xml --cov-report=term'
                }
                
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    try {
                        echo 'Performing Code Analysis'
                        sh '''
                        sonar-scanner \
                          -Dsonar.host.url=$SONAR_URL \
                          -Dsonar.token=$SONAR_TOKEN
                        '''
                        echo 'Code Analysis Completed'
                    } catch (Exception e) {
                        error "SonarQube Analysis stage failed: ${e.message}"
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    try {
                        echo 'Deploying application...'
                        // Add deployment commands here
                    } catch (Exception e) {
                        error "Deploy stage failed: ${e.message}"
                    }
                }
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
            node('any') {
                echo 'Cleaning up workspace...'
                cleanWs()
            }
        }
    }
}
