Galaxy Applications
=================

Quick setup
------------

* Download local copy of [galaxy](https://wiki.galaxyproject.org/Admin/GetGalaxy)
* Checkout latest release: `git checkout release_15.01`
* Create `config/galaxy.ini` as a copy of `config/galaxy.ini.sample`
* Configure `tools_config_file`, `check_migrate_tools` and `watch_tools` properties
* Minimal `tool_conf.xml`
    ```<?xml version='1.0' encoding='utf-8'?>
    <toolbox>
    <section id="getext" name="Get Data">
        <tool file="data_source/upload.xml" />
        <tool file="data_source/ucsc_tablebrowser.xml" />
        <tool file="data_source/ebi_sra.xml" />
        <tool file="data_source/biomart.xml" />
    </section>
    <section id="jetbrains" name="JetBrains tools">
        <tool file="<PATH_TO_TOOLS>tools.xml" />
    </section>
    </toolbox>```

Useful links
------------
* Galaxy
 * [Develop apps](https://wiki.galaxyproject.org/Develop)
 * [Add tool tutorial](https://wiki.galaxyproject.org/Admin/Tools/AddToolTutorial)
* Biolabs
 * Our [homepage](http://beta-research.jetbrains.org/groups/biolabs)
 * Our [wiki](http://biolabs.intellij.net)
 * Our NIH powered [genome browser](http://genomebrowser.labs.intellij.net)
 * [TeamCity](https://teamcity.jetbrains.com/project.html?projectId=Epigenome)
