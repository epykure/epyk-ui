# TODO Move this logic to NodeJs
from pathlib import Path
import shutil
from calmjs.parse import io
from calmjs.parse import es5
from calmjs.parse.unparsers.es5 import minify_print
from typing import List, Union


def get_files(path: Union[str, Path] = None) -> List[Path]:
  """ Get the list of JavaScript files to minify

  :param path: Path with JavaScript modules
  :return: List of files to be minified
  """
  path = path or Path(__file__).resolve().parent.parent
  files = []
  for p in Path(path, "js").glob('**/*'):
    if p.is_file():
      files.append(p)
  return files


def clear_dst(path: Union[str, Path] = None):
  """ Clear the existing internal native directory (used by Epyk framework) """
  path = path or Path(__file__).resolve().parent.parent
  dst_path = Path(path, "epyk", "core", "js", "native")
  if dst_path.exists():
    shutil.rmtree(dst_path)


def copy_files(js_files: List[Path]):
  """ Copy the minified files to the code / native folder.

  This is only working using ES5 rules so in case of error the files will not be converted.
  This will be addressed when migration to NodeJs.

  :param js_files: The list of Js files to minify
  :return:
  """
  replace_str = Path(Path(__file__).resolve().parent.parent, "js")
  dest_path = Path(Path(__file__).resolve().parent.parent, "epyk", "core", "js", "native")
  dest_path.mkdir(parents=True, exist_ok=True)
  for file in js_files:
    dst_file_path = Path(str(file).replace(str(replace_str), str(dest_path)))
    if not dst_file_path.parent.exists():
      dst_file_path.parent.mkdir(parents=True)
    try:
      js_min = io.read(es5, open(file))
      min_content = minify_print(js_min, obfuscate=True)
      Path(dest_path).mkdir(parents=True, exist_ok=True)
      with open(dst_file_path, "w") as min_js:
        min_js.write(min_content)
    except:
      print(file)
      with open(file, "r") as src_js:
        with open(dst_file_path, "w") as min_js:
          min_js.write(src_js.read())


if __name__ == "__main__":
  files = get_files()
  clear_dst()
  copy_files(files)
