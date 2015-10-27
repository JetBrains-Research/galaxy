Galaxy Applications
=================

Quick setup
------------

* Download local copy of [galaxy](https://wiki.galaxyproject.org/Admin/GetGalaxy)
* Checkout latest release: `git checkout release_15.01`
* Create `config/galaxy.ini` as a copy of `config/galaxy.ini.sample`
* Add the following line to `tool_conf.xml.sample`
```
    <section id="jetbrains" name="JetBrains tools">
        <tool file="<RELATIVE_PATH>/zinbra.xml" />
    </section>
```

Useful links
------------
* Galaxy
 * [Develop apps](https://wiki.galaxyproject.org/Develop)
 * [Add tool tutorial](https://wiki.galaxyproject.org/Admin/Tools/AddToolTutorial)
 * [Zinbra on Main tools Shed resource](https://toolshed.g2.bx.psu.edu/view/jetbrains/zinbra)
 * [Biostar Galaxy](https://biostar.usegalaxy.org)
* Biolabs
 * Our [homepage](http://beta-research.jetbrains.org/groups/biolabs)
 * Our [wiki](http://biolabs.intellij.net)
 * Our NIH powered [genome browser](http://genomebrowser.labs.intellij.net)
 * [TeamCity](https://teamcity.jetbrains.com/project.html?projectId=Epigenome)
