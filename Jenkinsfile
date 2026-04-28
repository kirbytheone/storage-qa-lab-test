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
        echo "$WORKSPACE"
        ls -la "$WORKSPACE"

        docker run --rm \
          --volumes-from jenkins \
          -v /mnt/storage_qa:/storage \
          -w "$WORKSPACE" \
          -e STORAGE_PATH=/storage \
          python:3.12-slim \
          bash -c "
            echo '=== INSIDE CONTAINER ===' &&
            pwd &&
            ls -la &&
            pip install -r requirements.txt &&
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
