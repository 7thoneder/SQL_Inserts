pipeline {
  agent any
  stages {
    stage('Build SQL Inserts') {
      steps {
        bat 'py -3 insert.py'
      }
    }
    stage('Move SQL File') {
      steps {
        bat 'move SQL.txt C:\\JenkinsJobs\\SQL_Inserts'
      }
    }
  }
  post {
    always {
      junit 'build/reports/SQL_Inserts/Inserts.xml'

    }

  }
}