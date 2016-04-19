# MQ Install

echo 'deb http://www.rabbitmq.com/debian/ testing main' > /etc/apt/sources.list.d/rabbitmq.list
sudo apt-get update
sudo apt-get install rabbitmq-server

#enable Web management
rabbitmq-plugins enable rabbitmq_management

#enable mqtt
rabbitmq-plugins enable rabbitmq_mqtt

# Add User  Rabbit MQ
rabbitmqctl add_user admin zanrooadmin123

# Add User Permission
rabbitmqctl set_user_tags admin administrator
rabbitmqctl set_permissions -p / admin ".*" ".*" ".*"


Set Exchange

rabbitmqadmin publish exchange=amq.default routing_key=test payload="hello, world" Message published

# Set Policy
rabbitmqctl set_policy ha-all "^to_." '{"ha-mode":"all"}' --priority 0 --apply-to all
rabbitmqctl set_policy realtime "task_message_realtime" '{"message-ttl":600000}' --priority 0 --apply-to all
rabbitmqctl set_policy ex.mqtt "mqtt.topic" '{"ha-mode":"all"}' --priority 3 --apply-to exchanges
rabbitmqctl set_policy q.mqtt "^mqtt.subscription-mqttjs_*" '{"ha-mode":"all"}' --priority 3 --apply-to queues

# Set Queue

# /etc/Config
[
    {rabbit, [
        {log_levels, [{connection, error}]},
        {tcp_listen_options,
         [binary,
          {packet, raw},
          {reuseaddr, true},
          {backlog, 128},
          {nodelay, true},
          {exit_on_close, false},
          {keepalive, true}]}
    ]},
    {rabbitmq_mqtt, [
        {exchange, << "mqtt.topic" >>},
    {tcp_listeners, [1883]}]}
].

