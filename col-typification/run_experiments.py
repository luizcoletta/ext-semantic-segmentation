import subprocess
import os

from install_packages import install_all_packages

install_pkg = False
processes = (["exp1_training_vgg_unet.py"])

if (install_pkg):
    required_pkg_list = [('numpy', 'numpy'),
                     ('scipy', 'scipy'),
                     ('pandas', 'pandas'),
                     ('matplotlib', 'matplotlib'),
                     ('seaborn', 'seaborn'),
                     ('plotly', 'plotly'),
                     ('sklearn', 'sklearn'),
                     ('cv2', 'opencv-python'),
                     ('PIL', 'Pillow'),
                     ('tensorflow', 'tensorflow>=2.4.1'),
                     ('keras', 'keras'),
                     ('glob', 'glob'),
                     ('random', 'random'),
                     ('json', 'json'),
                     ('os', 'os'),
                     ('six', 'six'),
                     ('sys', 'sys'),
                     ('argparse', 'argparse'),
                     ('subprocess', 'subprocess'),
                     ('skbuild', 'scikit-build'),
                     ('cmake', 'cmake'),
                     ('keras_segmentation', 'git+https://github.com/luizfsc/col-semseg')]
    install_all_packages(required_pkg_list)

procs = []
for pname in processes:
    logfile = 'logs/' + os.path.splitext(pname)[0] + '.log'
    with open(logfile, 'w') as f:
        proc = subprocess.Popen(['python3', pname], stdout=f)
        procs.append(proc)

for proc in procs:
    proc.wait()