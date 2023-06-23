import subprocess
from epyk.web import node


class Svelte(node.Node):
    def create(self, name: str):
        """
        To create a new project, run:

        Related Pages:

          https://svelte.dev/docs

        :param name: String. The application name
        """
        if name is None:
            subprocess.run('npm create svelte@latest --help', shell=True, cwd=self._app_path)
        else:
            subprocess.run('npm create svelte@latest %s' % name, shell=True, cwd=self._app_path)

    def install(self, name: str = None):
        if not name:
            subprocess.run('npm install', shell=True, cwd=self._app_path)
        else:
            subprocess.run('cd %s;npm install' % name, shell=True, cwd=self._app_path)

    def serve(self, name: str = None):
        """

        """
        if not name:
            subprocess.run('npm run dev', shell=True, cwd=self._app_path)
        else:
            subprocess.run('cd %s;npm run dev' % name, shell=True, cwd=self._app_path)
