pipeline {
    agent any

    triggers {
        cron('0 6 * * *')  // Runs at 6 AM daily
    }

    environment {
        VENV_PATH = "/Users/sonal/Playwright/venv"
        SCRIPT_PATH = "/Users/sonal/Playwright/tests/your_script.py"
    }

    stages {
        stage('Run Script') {
            steps {
                sh '''
                    source $VENV_PATH/bin/activate
                    python $SCRIPT_PATH
                '''
            }
        }
    }
}

