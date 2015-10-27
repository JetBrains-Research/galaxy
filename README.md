Galaxy Applications
=================

Quick setup
------------

* Download local copy of [galaxy](https://wiki.galaxyproject.org/Admin/GetGalaxy)
* Checkout latest release: `git checkout release_15.01`
* Create `config/galaxy.ini` as a copy of `config/galaxy.ini.sample`
* Configure `tools_config_file`, `check_migrate_tools` properties
* Minimal `tool_conf.xml`
```
    <?xml version='1.0' encoding='utf-8'?>
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
    </toolbox>
```

Useful links
------------
* Galaxy
 * [Develop apps](https://wiki.galaxyproject.org/Develop)
 * [Add tool tutorial](https://wiki.galaxyproject.org/Admin/Tools/AddToolTutorial)
 * [Tool config format](https://wiki.galaxyproject.org/Admin/Tools/ToolConfigSyntax)
 * [Quick reStructured text](http://docutils.sourceforge.net/docs/user/rst/quickref.html)
 * [Main tools Shed resource](https://toolshed.g2.bx.psu.edu/repository)
 * [Bed tools Shed example](https://github.com/galaxyproject/tools-iuc/blob/master/packages/package_bedtools_2_24/tool_dependencies.xml)
 * [Biostar Galaxy](https://biostar.usegalaxy.org)
* Biolabs
 * Our [homepage](http://beta-research.jetbrains.org/groups/biolabs)
 * Our [wiki](http://biolabs.intellij.net)
 * Our NIH powered [genome browser](http://genomebrowser.labs.intellij.net)
 * [TeamCity](https://teamcity.jetbrains.com/project.html?projectId=Epigenome)
