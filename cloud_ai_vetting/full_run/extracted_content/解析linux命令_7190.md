# 解析Linux命令
**URL:** https://explainshell.com
**Page Title:** explainshell.com - match command-line arguments to their help text
--------------------

- about
- theme Light Dark
- Light
- Dark
[LINK: showthedocs](http://showthedocs.com)

### examples

- :(){ :|:& };:
- for user in $(cut -f1 -d: /etc/passwd); do crontab -u $user -l 2>/dev/null; done
- file=$(echo `basename "$file"`)
- true && { echo success; } || { echo failed; }
- cut -d ' ' -f 1 /var/log/apache2/access_logs | uniq -c | sort -n
- tar zcf - some-dir | ssh some-server "cd /; tar xvzf -"
- tar xzvf archive.tar.gz
- find . -type f -print0
- ssh -i keyfile -f -N -L 1234:www.google.com:80 host
- git log --graph --abbrev-commit --pretty=oneline origin..mybranch

--------------------