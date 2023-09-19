## Cloudflare ddns
help: contact@himelrana.com
## Amazon Linux 2 Startup Cloud9 IDE
place startup.sh file in your cloud9 environment
## Call startup
your server /etc/rc.local file should be like below
```bash
touch /var/lock/subsys/local
/bin/sh /home/ec2-user/environment/startup/startup.sh
```
## Make sure you have run this command after editign /etc/rc.local file
```bash
chmod +x /etc/rc.d/rc.local
```

## Enjoy . Happy Hacking!
