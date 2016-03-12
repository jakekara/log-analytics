Instructions
------------

1. Put all of your access logs in a folder named ./accesslogs
2. Run run.sh with the command:

   ./run.sh
   
3. That's it!

Troubelshooting
---------------
1. If your Apache logs are not formatted EXACTLY like mine, you'll need to rewrite the regular expression in analyzeall.py in the line that has the re.search() statement,
and likely modify the headers and dictionary assignments as well.
2. If your run.sh doesn't run, make sure it has executible permissions, with something like

   chmod 755 run.sh
