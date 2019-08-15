# RepairConsole
This is a console made to log audio equipment repairs onto a sql database.
The intended use-case is for technicians who want a simple way to log their repairs onto a remote database.
Future versions will extend configurability.

-Usage

The python file in this repository has no database information in it. You must add your own to the add_db() function.
Later this will be changed so that it can read the necessary information from a file.


It can be run using IDLE, or compiled for portabilities sake. I've had the best luck with Nuitka using the Visual Studio Compiler.
To compile it on windows, install Nuitka and Visual Studio and run the command:

python -m nuitka --standalone --windows-disable-console --plugin-enable=tk-inter --verbose repcon.py
from a elevated command line window.

I've not tried to compile it on Linux or MacOS. Anyone who has luck can contact me and I'll add the info to this readme.


The database is intended to be mySQL, but the queries are so simple that it may work with other SQL implementations.
As it stands, the client database must have a table named 'repairs'. It should have nine columns with the following labels:

'repairnumber'

This is the ID for the repair.

'firstname'

'lastname'

The name of the client.

'typeof'

What sort of equipment is the repair is for.

'model'

'manufacturer'

Self explanatory.

'statusof'

Where it is in the repair process.

'dateof'

The date the equipment was recieved.

'comments'


These are liable to be made alterable in future versions.


-Specifications

This was written in Python 3.7. It uses tkinter version 8.6 for it's GUI library. It connects to a mySQL database using 
mysql connector for python version 2.0.
