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
    stage('WS Cleanup') {
      steps {
        cleanWs(cleanWhenSuccess: true)
      }
    }
  post {
      always {
          junit 'build/reports/SQL_Inserts/SQL_Inserts.xml'
      }
    }
  }
}