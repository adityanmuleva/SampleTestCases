pipeline {
    agent any 

    environment {
        BUILD_ENV = 'production' 
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
                sh 'cd "$WORKSPACE" || exit 1'
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
                sh './venv/bin/python run_tests.py'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                echo 'Performing Code Analysis'
                sh 'sonar-scanner'
                echo 'Code Analysis Completed'
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
