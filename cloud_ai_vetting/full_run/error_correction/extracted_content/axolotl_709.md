# Axolotl
**URL:** https://axolotl.readthedocs.io/en/latest
**Page Title:** Axolotl - ez vuln record — axolotl latest documentation
--------------------

- Axolotl - ez vuln record
- Edit on GitHub
[LINK: Edit on GitHub](https://github.com/k1m0ch1/axolotl/blob/master/docs/index.rst)

## Axolotl - ez vuln record 

A simple bug reporting tools for bug hunter to input the finding and Host Identity, by record all the finding with git and without needs to install the tools.
This tools created trying to solve problem for pentester/ bug bounty hunter when they need to manage the host information or finding,
it becomes hard when you manage the document based, sometime rely on file you store on harddrive or cloud storage is hard to manage, and you need times to makes a report or statistic.
Another option, you can manage every finding with “any” pentest documentation tools, sometime with great feature generate documentation and statistic, but it comes with problem you need to pay, sometime you need to install on your server/local and have many requirement to install.
axolotl comes with a simple feature, and it want to keep it simple, you only need to install axolotl and git on your machine. It has a main purpose to store and collaborate all finding with your team or yourself, and axolotl process the data to simplify lookup data, make a simple statistic and generate a simple report.
Axolotl inspired from [nuclei]( https://github.com/projectdiscovery/nuclei ) project, where I’m using nuclei as the collaboration tools for poc.
[LINK: https://github.com/projectdiscovery/nuclei](https://github.com/projectdiscovery/nuclei)

## How to Use 

Before everything else, you need to generate the directory structure of the axolotl, you can run this command
and by default you will got this structure directory
ok after you init the project, next you need to understand the use of this tools, this is the flow where axolotl used:
- whenever you want to assessment you need to understand about the Target, usually called reconaissance Process, so you need to input all the target Identity Information, this is called HostIdentity
whenever you want to assessment you need to understand about the Target, usually called reconaissance Process, so you need to input all the target Identity Information, this is called HostIdentity
to input new host identity you need to run this command
and the file will be generated and you can input the information as you need, or remove the unecessary field and will look like this
or you could see [Host-Identity-Format](.github/doc/Host-Identity-Format.md) for full format
- and after you found some vuln you need to input new vuln from specific host, run this command to add a new vuln:
and after you found some vuln you need to input new vuln from specific host, run this command to add a new vuln:
the file will generated and you can input the information as you need, or remove the unecessary field and will look like this
and after that you can see the simple statistic by running this command

--------------------