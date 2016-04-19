import zrconnect
import sys

class SysAction():
    def vm_start(self):
        print 'VM Start...'
    def vm_restart(self):
        print 'VM Restart...'
    def vm_shutdown(self):
        print 'VM Shutdown...'

class SysConfig():
    def config_timezone(self):
        print 'Config TimeZone %Zone'
    def config_ulimit(self):
        print 'Ulimit %s MB Config'

class ServiceAction():
    def start(self):
        print '%Service Start'
    def restart(self):
        print '%Service Restart'
    def stop(self):
        print '%Service Stop'


class InstallService():
    def git_pull_code(self):
        print 'CodePulling from GitHub'
        git pull %servicename
    def hg_pull_code(self):
        hg pull %servicename
        print 'CodePulling from BitBucket'
    def config_upstart(self):
        ref servicename
        echo upstart path >> /etc/init.d/%servicename.conf
        print 'Upstart %ServiceName Installed'

class PreInstall():
    def show_output(self):
        print 'Show Package'
    def install_node(self):
        print 'NodeJS Installing...'
        print 'NodeJS Version %s Install Complete'
    def install_go(self):
        print 'GoLang Installing...'
        print 'GoLang Version %s Install Complete'
    def install_es(self):
        print 'ElasticSearch Installing...'
        print 'ElasticSearch Version %s Install Complete'
    def install_mq(self):
        print 'RabbitMQ Installing...'
        print 'RabbitMQ Version %s Install Complete'
    def install_nginx(self):
        print 'Nginx Installing...'
        print 'Nginx Version %s Install Complete'

class ClusterRedis():
    def install_redis(self):
        print 'Redis Installing...'
        print 'Redis Version %s Install Complete'
    def clustering(self):
        print 'Configure'

class ClusterMongo():
    def install_mongo(self, ymlip, ymlkey):
        print 'MongoDB Installing...'
        print 'MongoDB Version %s Install Complete'
    def install_mongos(self):
        print 'Mongos Installing...'
        print 'Mongos Version %s Install Complete'
    def install_shard(self):
        print 'Mongo Shard Configure'
    def install_arbitor(self):
        print 'Mongo Arbitor Configure'
    def config_upstart(self):
        print 'Upstart Service Configure'

class ClusterEs():
    def install_es_master(self):
        print 'ElasticSearch Master Installing...'
        print 'ElasticSearch Master Version Install Complete'
    def install_es_data(self):
        print 'ElasticSearch Data Installing...'
        print 'ElasticSearch Data Version Install Complete'
    def install_es_client(self):
        print 'ElasticSearch Client Installing...'
        print 'ElasticSearch Client Version Install Complete'

class MigrateDB():
    def migrate_mongo(self):
        print 'migrateing mongo'
    def migrate_es(self):
        print 'migrateing elasticsearch'
    def migrate_queue(self):
        print 'migrating queue'