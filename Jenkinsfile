pipeline {
	agent { docker { image 'python:3.5.1' } } 
	stages {
		stage('run') {
			steps {
				sh 'python --version'
		        }
		}
	}
}
