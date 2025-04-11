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

that's it. so change the 2 workflows to your name and email. replace the example plugin, containing the necessary files. run the release action and wait a minute. modify template.txt to your content and visual taste, and run the makemd action to update the readme. on every plugin update or new plugin just run the release action. everything fully automated ;)