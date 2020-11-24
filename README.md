# cloudssp

## Searching For Your Site
<p> First you need to eee if your target is running cpanel, https://target.com/cpanel
  or use subdomainscanner and see if it has a www.cpanel.target.com if so the target might be vulnerable.</p>

<p> Looks like the site does not have the cpanel redirect on the main, lets check the subdomains And looks like we found www.cpanel.target.com, www.webmail.target.com, www.mail.target.com Okay so lets check if they have the service mailman running. www.webmail.target.com/mailman > 404 www.mail.taregt.com/mailman/ > 200 Okay, exploit time!</p>

<img src="https://imgur.com/5OgcSEd.jpg" data-canonical-src="https://imgur.com/5OgcSEd.jpg" style="max-width:50%;">
<img src="https://imgur.com/2sNGZZa.jpg" data-canonical-src="https://imgur.com/2sNGZZa.jpg" style="max-width:50%;">

## Exploiting

```bash
requires > python3
requires > requests, colorama
```

```bash
python3 exploit.py
```
<img src="https://cdn.discordapp.com/attachments/778381865987735565/780868103818051624/unknown.png" style="max-width:50%;">


