"""Build a public-only Cloud Run context without uploading the source workspace."""
from pathlib import Path
import shutil
import tempfile

from catalog import ROOT, build


def stage(root=ROOT):
    root = Path(root)
    parent = root / '.preview'
    parent.mkdir(exist_ok=True)
    target = Path(tempfile.mkdtemp(prefix='toolindex-cloudrun-', dir=parent))
    for filename in ('Dockerfile', 'nginx.conf'):
        shutil.copy2(root / 'deploy/cloudrun' / filename, target / filename)
    # A fresh build prevents unrelated files left in a previous dist from shipping.
    with tempfile.TemporaryDirectory(prefix='toolindex-public-build-') as directory:
        clean = Path(directory)
        for name in ('site', 'data'):
            shutil.copytree(root / name, clean / name)
        build(clean)
        shutil.copytree(clean / 'dist', target / 'public')
    return target


if __name__ == '__main__':
    print(stage())
