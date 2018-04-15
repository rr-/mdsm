# mdsm
Send e-mails directly to your local maildir.
No postfix, no sendmail, no nothing, just regular filesystem operations.

### Motivation

I made it because I wanted to receive e-mail alerts from local cronjobs and
since I happen to use maildir+neomutt, rather than setting up a whole SMTP
server, I only need to put a file into a proper destination.

### Supported features

- Simple
- Lets you control basic headers: sender, recipient and subject
- Tries to take a guess where your maildir is
- If `mdsm` fails to find your maildir, you can instruct it to use a default
  path in `$XDG_CONFIG_HOME/mdsm.conf`:

  ```
  maildir=~/mymail
  ```
