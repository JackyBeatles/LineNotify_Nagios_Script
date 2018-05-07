# LineNotify_Nagios_Script


#### Open the Nagios commnad configuration add new lines below it 

``` # vi  /etc/nagios/objects/commands.cfg ```

``` # 'notify-service-by-line' command definition
define command{
        command_name    notify-service-by-line
        command_line    /usr/bin/printf "%b" "***** Icinga *****\n\nNotification Type: $NOTIFICATIONTYPE$\n\nService: $SERVICEDESC$\nHost: $HOSTALIAS$\nAddress: $HOSTADDRESS$\nState: $SERVICESTATE$\n\nDate/Time: $LONGDATETIME$\n\nAdditional Info:\n\n$SERVICEOUTPUT$\n" >> /tmp/notify-service.txt | /etc/icinga/objects/line_nagios.py
        }
```

#### Open the Nagios contacts configuration add new line below it 
```
define contact{
      service_notification_commands   notify-service-by-line
}
```
![image](https://user-images.githubusercontent.com/1269261/39694725-7ed1869e-5212-11e8-9549-589f75435d5e.png)


