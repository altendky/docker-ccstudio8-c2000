#!/usr/bin/env python3

import os
import subprocess
import sys


def main():
    repository = (
        'http://software-dl.ti.com'
        '/dsps/dsps_public_sw/sdo_ccstudio/codegen/Updates/p2linux'
    )

    ius = (
        'com.ti.cgt.c2000.{}.linux.feature.group'.format(
            os.environ['COMPILER_VERSION']
        ),
    )

    subprocess.run(
        [
            'ccstudio',
            '-application', 'org.eclipse.equinox.p2.director',
            '-noSplash',
            '-repository', repository,
            '-installIUs', ','.join(ius),
        ],
        check=True
    )


if __name__ == '__main__':
    sys.exit(main())
