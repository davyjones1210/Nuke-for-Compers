# help(nuke.sample)

the_node = nuke.toNode('SAMPLE_ME')

# help(the_node.sample)

w = the_node.width()
h = the_node.height()

x = 0
y = 0
max_lum = 0
where = (0,0)

start = 1001
end = 1010

task = nuke.ProgressTask("Calc max luma px")
try:
    
    for frame in range(start, end):
        max_lum = 0
        where = (0,0)
        task.setMessage("Testing row {y}".format(y=y))
        if task.isCancelled():
            raise StopIteration()
        for y in range(0, h):
            task.setMessage("Testing row {y}".format(y=y))
            if task.isCancelled():
                raise StopIteration()
            for x in range (0, w):
                
                red = the_node.sample("rgba.red", x+0.5, y+0.5, frame=frame)
                green = the_node.sample("rgba.green", x+0.5, y+0.5, frame=frame)
                blue = the_node.sample("rgba.blue", x+0.5, y+0.5, frame=frame)
                
                luminance = 0.2126*red + 0.7152*green + 0.0722*blue
                if luminance > max_lum:
                    max_lum = luminance
                    where = (x,y)
        
        print(where)
        nuke.tprint(where)

except StopIteration:
    # Clean up and anything we want here. User has cancelled.
    nuke.message("Cancelled")

finally:
    del(task)
    





nuke.tprint("Hello world!")
sys.stderr.write("\nHellooo")
sys.stdout.write("123123")
    
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
    
    
