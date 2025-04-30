pipeline {
    agent any

    triggers {
        cron('0 6 * * *')  // Runs at 6 AM daily
    }

    environment {
        VENV_PATH = "/Users/sonal/Desktop/Playwright/playwright/venv"
        SCRIPT_PATH = "/Users/sonal/Desktop/Playwright/playwright/tests/Stuttgart_Appointment/appoint_eAT.py"
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

