pipeline {
         agent any
         stages {
                 stage('One') {
                 steps {
                     sh 'pip3 -V'
                 }
                 }
                 stage('Two') {
                 steps {
                    input('Do you want to proceed?')
                 }
                 }
                 stage('Three') {
                 steps {
                       sh 'python3 pysy.py'
                 }
              }
         }
}
