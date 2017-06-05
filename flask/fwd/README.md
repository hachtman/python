Initialisation:

At root, each is a Flask application instance.

The web server passes all reqs to this object instance for handling, using a protocol called Web Server Gateway Influence.

The flask constructor requires the main module. For most applications, pythons name variable is the correct arg.

We use the if name == main syntax because it assumes the app  is only the main instance when it is the file being run. If it is imported from another file, it will not be main and the interpreter will only define the function etc in the file, not run it.
