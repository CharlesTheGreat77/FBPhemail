# FBPhemail
Advanced Spear Phishing
Facebook Phishing Emailer
```
▬▬▬▬.◙.▬▬▬▬
  ▂▄▄▓▄▄▂                                                        ╫►►        ▁▁ ▓
◢◤ █▀▀████▄▄▄▄▄▄▄◢◤            ● ● ● ▄▄▄▄▄▄▄████▮                ╫       █████████
█  Gabes   GITHUB █▀▀▀▀╬            ▂▃▄▅████▀▀▀████▅▄            ╫    ▟██⍁██⍁██⍁███▙
◥█████████◤                       ▄█████ FBPhemail █████▄       ▜████ LEARN PYTHON ████▛
══╩════╩══                         ◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲◤         ▜███████████████████▛╬
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```
### SETUP
* Enter gmail address and password on line 6:
```
yag = yagmail.SMTP({'EMAIL@gmail.com':'Facebook'}, 'PASSWORD')
```

### FACEBOOK ACCESS TOKEN
```
grab a Facebook access token (free by creating a Facebook webpage) and put your access token in the HTML function
* under def html
```

#### Usage
* Individual Targets
```
$ python3 FBPhemail.py -e <email_address> -fn <first_name> -u <phishing_url> -id <facebook_id> [verbose]
```
* List of targets
```
$ python3 FBPhemail.py -f <file> -u <phishing_url> [verbose]
```

### 509mil facebook leak Usage
```
$ cat <leak_file.txt> | grep -hnr "[target first_name]:[target last_name]:[female/male]:[city]" | tr ":" " " | awk '{print <column for emails>, $4, $3}' > output_file.txt
$ cat output_file.txt | tr " " ":" > output.txt
```
- I'll update the email column number ASAP**
- A guess would be after the phone number column, which is column $2

* Example
```
$ cat USA.txt | grep -hnr "@gmail" | tr ":" " " | awk '{print <email_column>, $4, $3 > output.txt
$ cat output.txt | tr " " ":" > output.txt
```
- first/last name, female/male, city simply narrow down the search of a target(s).

* [FILE FORMAT]
```
  email:first_name:facebook_id
```
* Example
```
  test@gmail.com:test:2138012931232
  test@yahoo.com:testing:3210231273211
```

### 👽 Information
**Hi there, I'm [Charles](https://github.com/CharlesTheGreat77). 👋 Python Developer from the United States.** 

[<img src ="https://img.shields.io/badge/🌐-CharlesTheGreat77.github.io-%23.svg?style=for-the-badge&logo=&logoColor=white%22">](https://CharlesTheGreat77.github.io/)

### 🛠 Technologies & Tools

![HTML5](https://img.shields.io/badge/-HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![Sublime Text](https://img.shields.io/badge/-Sublime-4B4B4B?style=flat-square&logo=sublime-text&logoColor=FF9800)
<a href="https://github.com/priyanshumay"><img src="https://img.shields.io/badge/python-FFFF00.svg?style=for-the-badge&logo=python&logoColor=0768a8&labelColor=ffffff" alt="python"></a>

...

### 💬 Contact Me 

![Gmail Badge](https://img.shields.io/badge/-doobthegoober@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white)

### 🚦 Stats

<a href="https://github.com/CharlesTheGreat77">
  <img src="https://github-readme-stats.vercel.app/api?username=CharlesTheGreat77&show_icons=true&hide=commits" />
</a>
<a href="https://github.com/CharlesTheGreat77">
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=CharlesTheGreat77&layout=compact" />
</a>

<p align="center"> 
  <img src="https://profile-counter.glitch.me/CharlesTheGreat77/count.svg" />
</p>

---
⭐️ From [Charles](https://github.com/CharlesTheGreat77)
