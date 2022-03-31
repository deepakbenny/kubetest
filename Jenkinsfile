node {
    def app
    stage('Clone repository') {
        checkout scm
    }
    stage('Build image') {
       app = docker.build("fatninja/kubetest")
    }
    stage('Push image') {
        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
            app.push("${env.BUILD_NUMBER}")
        }
    }
    stage('Update GIT') {
            script {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    withCredentials([usernamePassword(credentialsId: 'github', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                        //def encodedPassword = URLEncoder.encode("$GIT_PASSWORD",'UTF-8')
                        sh "git config user.email deepakbenny@outlook.com"
                        sh "git config user.name deepakbenny"
                        //sh "git switch master"
                        sh "cat deployment.yaml"
                        sh "sed -i 's+fatninja/kubetest.*+fatninja/kubetest:${env.BUILD_NUMBER}+g' deployment.yaml"
                        // sh "cat deployment.yaml"
                        sh "git add ."
                        sh "git commit -m 'Updating maniftest file: Done by Jenkins Job changemanifest: ${env.BUILD_NUMBER}'"
                        sh "git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/${GIT_USERNAME}/kubernetesmanifest.git HEAD:master"
                        }
                }
            }
    }
}