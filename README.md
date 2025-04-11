# **my endless-sky-plugins**
instructions:<br>


.github/workflows/(manual) create release.yml
<ul>
  <li>change 'git config user.name "zuckung"' to your username</li>
  <li>change 'git config user.email "zuckung@gmx.de"' to your email</li>
  <li>this is the workflow you use for releasing a plugin. after plugin upload, go to action tab, click the workflow, click run workflow, enter the exact plugin name(else it fails) and let it run(it takes a minute to finish). it puts outs a release with an asset zip and with an increasing version number, noted in /res/versioning.txt. this workflow also generates the readme.md taking in all plugins, screenshots, the newly generated asset zip and other data. so never edit the readme, it gets overwritten on release.</li>
</ul>    
    
.github/workflows/(manual) make md.yml
<ul>
  <li>change 'git config user.name "zuckung"' to your username</li>
  <li>change 'git config user.email "zuckung@gmx.de"' to your email</li>
  <li>this workflow is also run manually in case you want to change the readme without pushing a release. it does the same as the previous workflow just without the release. the readme content (beside the variable content, like plugins) is read out of res/template.txt</li>
</ul>

.github/workflows/(on push) spellcheck.yml
<ul>
  <li>this workflow runs on every push and checks for spelling errors. it fails if an error is found.</li>
  <li>.codespell.exclude and .codespell.words.exclude can be edited to whitelist words, currently filled with my excludes as an example</li>
</ul>

.github/workflows/(on push) data check.yml
<ul>
  <li>this workflow runs on every push and checks for ES script errors. it fails if an error is found.</li>
  <li>that is done by starting the game on the github server, loading the plugins and reporting errors.</li>
</ul>


myplugins/example.plugin
<ul>
  <li>delete it and put yours there</li>
  <li>it needs an icon.png, an about.txt and a data folder, and preferably its own readme.md, so the readme can get generated out of these data</li>
  <li>name your plugin without spaces or special characters. that is because when releasing github replaces them with a '.'. or maybe the release action does that, not sure.</li>
  <li></li>
</ul>


res/template.txt
<ul>
  <li>from here comes the static readme.md content. this textfile is splitted into 2 part, the upper static content, like what you are reading now, and the variable plugin template, separated by 'plugin template below this line'. each plugin gets this plugin template. it works with variables put between '%variablename%'. these get replaced on generation. both parts can be mixed in html and markdown. experiment. i.e 'description' variable gets replaced by the content from about.txt, 'size' by kb/mb size, 'readme' by the plugin readme.md etc.</li>
<ul>

res/news.txt
<ul>
  <li>when releasing a plugin a new entry is made automatically, but manual entries work too.</li>
</ul>

res/versioning.txt
<ul>
  <li>if the plugin isn't in that textfile it gets written to this file and set to version '1.0.0'. with every run it increases by '0.0.1'. manually changing that works. i.e. setting version to '1.1.0' or' 2.4.0' in versioning.txt.</li>
</ul>

res/src
<ul>
  <li>python files. no need to touch them. the news box or the pluginlist variables get their content from here.</li>
</ul>

res/imagemd
<ul>
  <li>with every readme.md generation(from manual readme.generation or manual release) for every plugin an .md file gets generated, containing all image files of that plugin. the link to it is shown in the plugin template with the 'pluginmd' variable</li>
</ul>

screenshots/
<ul>
  <li>if you have screenshots put them into the screenshot folder and name them after the plugin. i.e. example.plugin01.jpg, example.plugin02.jpg ... these screenshots are shown in the plugin template with the 'screenshots' variable</li>
</ul>

inside the repo settings
<ul>
  <li>actions>general: activate Allow all actions and reusable workflows</li>
  <li>actions>general: workflow permissions: activate Read and write permissions </li>
</ul>



that's it. so change the 2 workflows to your name and email. replace the example plugin, containing the necessary files. run the release action and wait a minute.
  


## Latest News:
<table><tr><td><img width="882" height="1"><br>2025-04-11 | update: Pirate Start<br>
2025-04-10 | initial repository setup<br>
<img width="882" height="1"><br></td></tr></table>

## Plugin List:<br>
<table><tr valign="top"><td><img width="294" height="1"><br>
<a href="README.md#Pirate Start">Pirate Start</a><br>
<a href="README.md#PugGalaxyContent">PugGalaxyContent</a><br>
<a href="README.md#Remant Swan">Remant Swan</a><br>
<img width="294" height="1"><br></td><td><img width="294" height="1"><br>
<a href="README.md#Unused Vanilla Content">Unused Vanilla Content</a><br>
<a href="README.md#bunrodea rebellion">bunrodea rebellion</a><br>
<img width="294" height="1"><br></td><td><img width="294" height="1"><br>
<a href="README.md#predecessor gas giant">predecessor gas giant</a><br>
<a href="README.md#reloadable nukes">reloadable nukes</a><br>
<img width="294" height="1"><br></td></tr></table>





---

### Pirate Start

<img src="myplugins/Pirate Start/icon.png" height="100">

[Pirate.Start.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0-Pirate.Start/Pirate.Start.zip) | N/A | N/A | [view files](https://github.com/geojak/YouKnowWho-s-ES-Plugins/tree/main/myplugins/Pirate%20Start/) | <a href="res/imagemd/Pirate Start.md">view images</a> [2]<br>
<br>
>Pirate Start
>
>1. New Pirate Game Start
>2. Pirate Rehab Mission chain and Fake Id, 2 ways out of crime
<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>Pirate Start



1. New Pirate Game Start

2. Pirate Rehab Mission chain and Fake Id, 2 ways out of crime
</blockquote>
</details>

<br>


---

### PugGalaxyContent

<img src="myplugins/PugGalaxyContent/icon.png" height="100">

[PugGalaxyContent.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0-PugGalaxyContent/PugGalaxyContent.zip) | N/A | N/A | [view files](https://github.com/geojak/YouKnowWho-s-ES-Plugins/tree/main/myplugins/PugGalaxyContent/) | <a href="res/imagemd/PugGalaxyContent.md">view images</a> [4]<br>
<br>
>PugGalaxyContent
>
>Adds some more systems in the Pug Galaxy, a stranded wanderer faction and another pug planet to farm.

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>PugGalaxyContent



Adds some more systems in the Pug Galaxy, a stranded wanderer faction and another pug planet to farm.

</blockquote>
</details>

<br>


---

### Remant Swan

<img src="myplugins/Remant Swan/icon.png" height="100">

[Remant.Swan.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0-Remant.Swan/Remant.Swan.zip) | N/A | N/A | [view files](https://github.com/geojak/YouKnowWho-s-ES-Plugins/tree/main/myplugins/Remant%20Swan/) | <a href="res/imagemd/Remant Swan.md">view images</a> [1]<br>
<br>
>Remnant Swan
>
>Adds the Swan to the remants and the Inhibitor Turret, reusing assets from vanilla. Rebalanced by me.
<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>Remnant Swan



Adds the Swan to the remants and the Inhibitor Turret, reusing assets from vanilla. Rebalanced by me.
</blockquote>
</details>

<br>


---

### Unused Vanilla Content

<img src="myplugins/Unused Vanilla Content/icon.png" height="100">

[Unused.Vanilla.Content.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0-Unused.Vanilla.Content/Unused.Vanilla.Content.zip) | N/A | N/A | [view files](https://github.com/geojak/YouKnowWho-s-ES-Plugins/tree/main/myplugins/Unused%20Vanilla%20Content/) | <a href="res/imagemd/Unused Vanilla Content.md">view images</a> [6]<br>
<br>
>Unused Vanilla Content
>
>This plugin adds a ton of things:
>1. Added unused vanilla ships to the game, you will see a lot more pirate fleet variants: Nighthawk, Waverider, Valkyrie, Modified Osprey, Modified Vanguard
>2. This plugin contains Kestrel.Unlocks from zuckung
>3. Made New Tibet and Girtarb Tributable
>4. The unfettered hai start using their protye weapons Ionic Blaster, Ionic Turret and Ionic Shredder during the wanderer invasion
>5. This Plugin reenables Hai Reveal
>6. Unfettered start using the modified Ladybug during Hai Reveal
>7. You can steal a Unfettered ID by boarding them, which allows you to buy the new prototype weapons
>8. You can continue to trade jump drives to the Unfettered even after you helped the Wanderers
<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>Unused Vanilla Content



This plugin adds a ton of things:

1. Added unused vanilla ships to the game, you will see a lot more pirate fleet variants: Nighthawk, Waverider, Valkyrie, Modified Osprey, Modified Vanguard

2. This plugin contains Kestrel.Unlocks from zuckung

3. Made New Tibet and Girtarb Tributable

4. The unfettered hai start using their protye weapons Ionic Blaster, Ionic Turret and Ionic Shredder during the wanderer invasion

5. This Plugin reenables Hai Reveal

6. Unfettered start using the modified Ladybug during Hai Reveal

7. You can steal a Unfettered ID by boarding them, which allows you to buy the new prototype weapons

8. You can continue to trade jump drives to the Unfettered even after you helped the Wanderers
</blockquote>
</details>

<br>


---

### bunrodea rebellion

<img src="myplugins/bunrodea rebellion/icon.png" height="100">

[bunrodea.rebellion.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0-bunrodea.rebellion/bunrodea.rebellion.zip) | N/A | N/A | [view files](https://github.com/geojak/YouKnowWho-s-ES-Plugins/tree/main/myplugins/bunrodea%20rebellion/) | <a href="res/imagemd/bunrodea rebellion.md">view images</a> [1]<br>
<br>
>Bunrodea Rebellion
>
>The Megasa had enough of the Tyrant Queen. It is time for war. Which side will you support?

<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>Bunrodea Rebellion



The Megasa had enough of the Tyrant Queen. It is time for war. Which side will you support?

</blockquote>
</details>

<br>


---

### predecessor gas giant

<img src="myplugins/predecessor gas giant/icon.png" height="100">

[predecessor.gas.giant.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0-predecessor.gas.giant/predecessor.gas.giant.zip) | N/A | N/A | [view files](https://github.com/geojak/YouKnowWho-s-ES-Plugins/tree/main/myplugins/predecessor%20gas%20giant/) | <a href="res/imagemd/predecessor gas giant.md">view images</a> [1]<br>
<br>
>Predeceesor Gas Giant
>
>An ancient hidden station in the clouds of a gas giant - Will you open pandoras box?
<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>Predeceesor Gas Giant



An ancient hidden station in the clouds of a gas giant - Will you open pandoras box?
</blockquote>
</details>

<br>


---

### reloadable nukes

<img src="myplugins/reloadable nukes/icon.png" height="100">

[reloadable.nukes.zip](https://github.com/zuckung/endless-sky-plugins/releases/download/v1.0-reloadable.nukes/reloadable.nukes.zip) | N/A | N/A | [view files](https://github.com/geojak/YouKnowWho-s-ES-Plugins/tree/main/myplugins/reloadable%20nukes/) | <a href="res/imagemd/reloadable nukes.md">view images</a> [3]<br>
<br>
>Reloadable Nukes
>
>Adds a normal functioning human nuke launcher and nuclear missile ammunition. The vanilla one time use nuke is unchanged.
<details>
<summary>:blue_book: Plugin readme</summary>
<blockquote>Reloadable Nukes



Adds a normal functioning human nuke launcher and nuclear missile ammunition. The vanilla one time use nuke is unchanged.
</blockquote>
</details>

<br>
