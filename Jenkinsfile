pipeline {
    agent any
    
    parameters {
        choice(name: 'ENV', choices: ['dev', 'prod'], description: 'Выберите окружение для деплоя')
    }
    
    options {
        cleanWs() // Очищает рабочую директорию после выполнения
    }
    
    stages {
        stage('Информация о деплое') {
            steps {
                script {
                    def environment = params.ENV
                    echo "Deploying to ${environment}"
                }
            }
        }
        
        stage('Копирование файлов на сервер') {
            steps {
                script {
                    def environment = params.ENV
                    
                    // Выбор конфигурации сервера в зависимости от окружения
                    def serverName = (environment == 'prod') ? 'prod-server' : 'dev-server'
                    
                    // Копирование файлов через SSH
                    sshPublisher(
                        publishers: [
                            sshPublisherDesc(
                                configName: serverName,
                                transfers: [
                                    sshTransfer(
                                        sourceFiles: '**/*', // Копировать все файлы
                                        remoteDirectory: '/var/www/app', // Папка на удаленном сервере
                                        execCommand: 'sudo systemctl restart app-service', // Дополнительная команда после копирования
                                        execTimeout: 120000
                                    )
                                ],
                                usePromotionTimestamp: false,
                                verbose: true
                            )
                        ]
                    )
                }
            }
        }
    }
    
    post {
        success {
            echo "Деплой в ${params.ENV} успешно завершен!"
        }
        failure {
            echo "Ошибка при деплое в ${params.ENV}"
        }
    }
}
