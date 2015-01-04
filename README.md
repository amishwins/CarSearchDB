CarSearchDB
===========

Extremely fun example using python to connect to a mysql db and then serve it up using bottle.


I hate the world
----------------
Attempted to host on a Linux box with LAMP + Python. Faced many issues:

1. Accessing guest localhost from host (enable bridge network settings in vbox)
1. Multiple versions of Python, and pip 
  * Built python from source, replaced it as default
  * Added an alias in ~/.bashrc (python=python3) [here](http://stackoverflow.com/questions/21509464/how-can-i-remove-a-version-of-python-in-ubuntu-12-04)
1. /usr/local/lib/python3.4/dist-packages doesn't seem to be inside sys.path
  * Workaround for now in routes.py, just manually sys.append the path
1. Couldn't installing the mysql python library
  * Did `$ sudo apt-get install python-mysqldb`, but not sure 
1. Default no access to dist-packages (chmod -R 775 that directory)
