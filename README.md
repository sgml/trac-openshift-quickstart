Trac on OpenShift
=================

This git repository helps you get up and running quickly with a Trac installation
on OpenShift.  The bankend database can by sqlite, MySQL or PostgreSQL, depending on
the cartridges that are installed when the application is launched.

This quickstart contains the base Trac installation, as well as TracAccountManager.

Running on OpenShift
--------------------

1. Create an account at http://www.openshift.com/ and install the client tools (run 'rhc setup' first)

2. Create a Python 2.7 application, with the cartridge containing the database you want.
   If you do not install a database cartridge at this time, the default sqlite database will be used.

   For example:

       rhc app create radiant python-2.7 mysql-5 --from-code=https://github.com/kelvinmo/trac-openshift-quickstart

3. You will need to create a Trac administration account manually.  SSH to the instance and run the
   following command:

   trac-admin $OPENSHIFT_DATA_DIR/trac/env permission add <user_name> TRAC_ADMIN

4. That's it, you can now checkout your application at:

    http://radiant-$yournamespace.rhcloud.com
    

Notes
=====

Source code repository
----------------------

You will need to set up access to the source code repository manually in the OpenShift data
directory.


Directories
-----------

The Trac environment directory is located at `$OPENSHIFT_DATA_DIR/trac`.

