pipeline {
    agent any

    stages {
        stage('Git') {
            steps {
                git branch: 'main', url: 'https://github.com/anwar789456/avec-maven.git'
            }
        }
   
        stage('Maven') {
            steps {
                echo 'Hello World'
            }
        }

        stage('Run Python Program') {
            steps {
                echo "Running factorial program..."
                sh '''
                    python3 fact.py
                '''
            }
        }
    }
}
