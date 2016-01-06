you can move the current folders into one of the current folders with the mv command

for example, I was able to bring up ls: hello_world/  projects/  template/
    mv * projects moved hello_world and template into the projects folders
    
the * is a "wildard" character.
    For example ls *.mp* will list any MP3, MP4 or MPG files in a directory. 
Note that this command will give a warning telling us that we are trying to move the projects directory (which is part of *) into itself. This can be safely ignored.
