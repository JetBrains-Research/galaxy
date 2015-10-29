Galaxy Applications
===================
* [cmeth](https://toolshed.g2.bx.psu.edu/view/jetbrains/cmeth) - a tool for analyzing and comparing BS-Seq data
* [zinbra](https://toolshed.g2.bx.psu.edu/view/jetbrains/zinbra) - a tool for analyzing and comparing ChIP-Seq data

Local setup
-----------

* Download local copy of [galaxy](https://wiki.galaxyproject.org/Admin/GetGalaxy)
* Checkout latest release: `git checkout release_15.01`
* Create `config/galaxy.ini` as a copy of `config/galaxy.ini.sample`
* Add the following line to `tool_conf.xml.sample`
```
    <section id="jetbrains" name="JetBrains tools">
        <tool file="<RELATIVE_PATH>/zinbra.xml" />
    </section>
```

Publish to tool shed
--------------------
* Copy application folder to dedicated hg repository
* Mention snapshot version in commit message
* Commit and push to mercurial
* Invoke **Repository Actions** | **Reset all repository metadata**
* Voila, tool shed version is synchronized with mercurial repo


Useful links
------------
* Galaxy
 * [Develop apps](https://wiki.galaxyproject.org/Develop)
 * [Add tool tutorial](https://wiki.galaxyproject.org/Admin/Tools/AddToolTutorial)
 * [Biostar Galaxy](https://biostar.usegalaxy.org)
* Biolabs
 * Our [homepage](http://beta-research.jetbrains.org/groups/biolabs)
 * Our [wiki](http://biolabs.intellij.net)
 * Our NIH powered [genome browser](http://genomebrowser.labs.intellij.net)
 * [TeamCity](https://teamcity.jetbrains.com/project.html?projectId=Epigenome)
