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
                sh 'source venv/bin/activate'  
            }
        }
        
        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'python run_tests.py'
            }
        }

        stage('Code Quality Check') {
            steps {
                echo 'Running static code analysis...'
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
