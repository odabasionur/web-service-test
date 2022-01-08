# Notes

## Version-2
- Failed\
`flask_nginx      | 2021/09/30 08:58:14 [emerg] 1#1: host not found in upstream "ws-app" in /etc/nginx/nginx.conf:20`\
`flask_nginx      | nginx: [emerg] host not found in upstream "ws-app" in /etc/nginx/nginx.conf:20`\
`flask_nginx exited with code 1`\
(No any response in localhost:4000/ (even nginx bad gateway) 
- Network_mode: host
- port binding in nginx is comment out
### Todos
- define container name in /etc/hosts (just to see if this is what it needs)
- remove ip in `app1/app1_uwsgi.ini` `socket`


## Version-1
- Succeed
- Bridge Network
- container name ~= app name (No need to define name in /etc/hosts)

