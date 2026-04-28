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
        echo "=== DEBUG WORKSPACE ==="
        pwd
        ls -la

        docker run --rm \
          -v "$PWD":/app \
          -v /mnt/storage_qa:/storage \
          -w /app \
          python:3.12-slim \
          bash -c "
            echo '=== INSIDE CONTAINER ===' &&
            pwd &&
            ls -la &&
            pip install -r requirements.txt &&
            pytest -v
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
