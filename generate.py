import requests, json, random, time, socket, platform
nameid = "ObadiahHarahap"
timestr = time.strftime("%Y-%m-%d - %H:%M:%S UTC")
f = open("./README.md", "w")
pokemon_id = random.randint(1, 151)
res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
result = json.loads(res.text)
f.write(f'''<p align="center">
    <img src="{result['sprites']['front_default']}" width="150" height="150">
</p>
<h3 align="center">You have been greeted by a wild <b>{result['name'].title()}</b></h3>
<h3 align="center">Have a nice day!</h3>
        
<p>
  <h1 align="center">
    <b>Hi there, I'm <a href="https://xcodl.github.io/{nameid}/">{nameid}</a> 👋</b>
  </h1>
</p>
<p align="center">
  <a href="https://github.com/{nameid}">
    <img alt="GitHub Stats" src="https://github-readme-stats.vercel.app/api?username={nameid}&hide=issues&hide_title=true&include_all_commits=true&bg_color=30,e96443,904e95&title_color=fff&text_color=fff" />
    </a>
</p>
#### This Page Create at:
<h3 align="center"><b>{timestr}</b></h3>
#### Create By Machine:
<h3 align="center"><b>{socket.gethostname()}</b></h3>
<h3 align="center"><b>{platform.platform()}</b></h3>
<h3 align="center"><b>{socket.gethostbyname(socket.gethostname())}</b></h3>
''')
f.close()
