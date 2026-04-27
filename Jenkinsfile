pipeline {
    agent any

    stages {
        stage('Check storage mount') {
            steps {
                sh '''
                test -d /mnt/storage_qa
                mountpoint /mnt/storage_qa
                df -h /mnt/storage_qa
                '''
            }
        }

        stage('Run tests in Docker') {
            steps {
                sh '''
                docker run --rm \
                  -v "$PWD":/app \
                  -v /mnt/storage_qa:/storage \
                  -w /app \
                  -e STORAGE_PATH=/storage \
                  python:3.12-slim \
                  bash -c "
                    pip install -r requirements.txt &&
                    ruff check . &&
                    black --check . &&
                    pytest -v --html=report.html --self-contained-html
                  "
                '''
            }
        }

        stage('Archive report') {
            steps {
                archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
}