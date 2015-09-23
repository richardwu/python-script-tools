# Python scripts for use in terminal

Collection of custom-written python scripts for use in terminal.


## Usage
You can either run the script directly from command line or add it to your bash profile.

### Run directly
`python foobar.py`

### Use via a command in bash (OSX and Linux)
1. Open your .bash_profile file

	* Vim:
	
		`vim ~/.bash_profile`
	* Default text editor:
		
		`open ~/.bash_profile`

	##### **NOTE: If .bash_profile does not exist, simply create one i.e. `touch ~/.bash_profile`

2. Add this to your .bash_profile
	```
	[name_of_function]() {
		python [path_to_file]/[name_of_python_script]
	}
	alias [desired_command]=[name_of_function]
	```
	If the function takes arguments, simply append $i to the command inside the bash function, where i = the index of the argument

	i.e. for 3 arguments `python [path_to_file]/[name_of_python_script] $1 $2 $3`

3. Restart bash/terminal shell

## Available scripts
### rgb_to_hex.py
Converts RGB values (3 arguments) to a hex string (used for web colors primarily).
