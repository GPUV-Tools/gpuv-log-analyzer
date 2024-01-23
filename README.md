## GPUV Log Analyzer

### How to setup
#### pip install -r requirements.txt

### Sample usage
python main.py -file [file name] -dest [file, terminal, all]

### Initial Milestones
#### input → wpp log
#### output → function name | how many times called | average, min, max call duration

### Tentative
#### output call stack, flame graph
#### organize by errors, warning, info, debug

### Scratch Notes
#### CLI interface
#### env setup using pipenv
####
multiple function calls close to each other
and we're missing some entries and exits

need to modify gpuv logging
f {

id = time()
enter(id)

exit(starting time: id)

}
