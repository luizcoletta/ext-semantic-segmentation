import pip

def install(package):
    pip.main(['install', package])

### https://stackoverflow.com/questions/48097428/how-to-check-and-install-missing-modules-in-python-at-time-of-execution
def install_all_packages(modules_to_try):
    for module in modules_to_try:
        try:
            __import__(module[0])
            print(">> " + module[0] + " already installed!")
        except ImportError as e:
            #install(e.name)
            install(module[1])