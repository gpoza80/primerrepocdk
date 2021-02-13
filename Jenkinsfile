pipeline {
  agent any
  stages {
    stage('Inicio_enviroment') {
      steps {
        echo 'Iniciando construccion de proyecto'
        sh 'env'
      }
    }

    stage('docker Env') {
      parallel {
        stage('docker Env') {
          steps {
            sh 'docker -v'
          }
        }

        stage('docker images') {
          steps {
            sh 'docker images'
          }
        }

      }
    }

    stage('Build') {
      steps {
        sh 'cat versionImage | xargs ./scripts/build.sh'
      }
    }

    stage('Run_Container') {
      steps {
        sh 'docker stop proyectoApi || true; docker rm proyectoApi || true; docker run --name proyectoApi -itd  -p 3001:3001 apache-centostest:3.1'
        sh 'docker ps'
      }
    }

  }
}