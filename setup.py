# A very simple setup script to create an executable.
#
# Run the build process by entering 'setup.py py2exe' or
# 'python setup.py py2exe' in a console prompt.
#
# If everything works well, you should find a subdirectory named 'dist'
# containing some files, among them hello.exe and test_wx.exe.


from distutils.core import setup
import py2exe

setup(
    # The first three parameters are not required, if at least a
    # 'version' is given, then a versioninfo resource is built from
    # them and added to the executables.
    version = "0.0.1",
    description = "Sarath's Keylogger",
    name = "Salk",

    # targets to build
    console = [
        {
            "script": "salk_dist.py",
            "dest_base": "salk_dbugger"
        }
    ],
    
    #windows = ["keylogger.pyw"],
    windows = [
       {
           "script": "salk_dist.py",
           "dest_base": "salk"
       }
    ],
    )

