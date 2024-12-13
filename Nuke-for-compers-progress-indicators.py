nuke.tprint('Hello world')

sys.stderr.write('What is up?')
sys.stdout.write('Nothin much')

import time



task = nuke.ProgressTask("Adoring kittens")


task.setProgress(10)
time.sleep(2)
if task.isCancelled():
    raise Exception()
task.setMessage("locating kittens")
task.setProgress(20)
time.sleep(2)
if task.isCancelled():
    raise Exception()
task.setMessage("listening for meows")
task.setProgress(40)
time.sleep(2)
if task.isCancelled():
    raise Exception()
task.setMessage("found kittens")
task.setProgress(80)
time.sleep(2)
if task.isCancelled():
    raise Exception()
task.setMessage("applying catnip")
task.setProgress(90)
time.sleep(2)
if task.isCancelled():
    raise Exception()
task.setMessage("done!")
task.setProgress(100)
time.sleep(2)

del(task)