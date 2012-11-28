import sublime, sublime_plugin, os, filename_switcher, glob

class AlternateSpecCommand(sublime_plugin.WindowCommand):

  cache = {}

  def run(self):
    filename = self.window.active_view().file_name()
    filename = os.path.basename(filename)
    filename = filename_switcher.switch(filename)
    fullpath = None

    if filename in self.cache:
      fullpath = self.cache[filename]

    if fullpath is None:
      fullpath = self.find_in_open_files(filename)

    if fullpath is None:
      fullpath = self.find_in_folders(filename)

    if fullpath:
      self.cache[filename] = fullpath
      self.window.open_file(fullpath)
    else:
      sublime.message_dialog("No file named '%s'" % filename)

  def find_in_open_files(self, filename):
    for view in self.window.views():
      if view.file_name():
        basename = os.path.basename(view.file_name())
        if basename == filename:
          return view.file_name()
    return None

  def find_in_folders(self, filename):
    for folder in self.window.folders():
      fullpath = self.find_in_folder(filename, folder)
      if fullpath:
        return fullpath
    return None

  def find_in_folder(self, filename, folder):
    for root, dirs, files in os.walk(folder):
      if filename in files:
        return os.path.join(root, filename)
    return None
