## LineNotify_Nagios_Script

add new line  vi  /etc/icinga/objects/commands.cfg 

``` # 'notify-service-by-line' command definition
define command{
        command_name    notify-service-by-line
        command_line    /usr/bin/printf "%b" "***** Icinga *****\n\nNotification Type: $NOTIFICATIONTYPE$\n\nService: $SERVICEDESC$\nHost: $HOSTALIAS$\nAddress: $HOSTADDRESS$\nState: $SERVICESTATE$\n\nDate/Time: $LONGDATETIME$\n\nAdditional Info:\n\n$SERVICEOUTPUT$\n" >> /tmp/notify-service.txt | /etc/icinga/objects/line_nagios.py
        }
```
