import os
import sys 
import time
import threading
import json
import datetime
from pathlib import Path
import zipfile

class Watcher(object):
    running = True
    refresh_delay_secs = 1

    # Constructor
    def __init__(self, watch_file, call_func_on_change=None, *args, **kwargs):
        self._cached_stamp = 0
        self.filename = watch_file
        self.call_func_on_change = call_func_on_change
        self.args = args
        self.kwargs = kwargs

    # Look for changes
    def look(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            self._cached_stamp = stamp
            # File has changed, so do something...
            if self.call_func_on_change is not None:
                self.call_func_on_change(*self.args, **self.kwargs)

    # Keep watching in a loop        
    def watch(self):
        while self.running: 
            try: 
                # Look for changes
                time.sleep(self.refresh_delay_secs) 
                self.look() 
            except KeyboardInterrupt: 
                print('\nDone') 
                break 
            except FileNotFoundError:
                print('File was not found. Please do not change A4.ipynb name nor change location relative to watcher.py. Rerun this cell once filename/location is fixed.')
                break
            except: 
                print('Stopping logging: Unhandled error: %s' % sys.exc_info())
                break

# Call this function each time a change happens
def logger(base_filename):
    src_path = os.path.realpath(base_filename)
    dir_path = os.path.dirname(src_path)
    
    historicalSize = -1
    while (historicalSize != os.path.getsize(src_path)):
      historicalSize = os.path.getsize(src_path)
      time.sleep(0.25)
    
    with open(src_path, 'r') as checkpoint_source:
        checkpoint = json.loads(checkpoint_source.read())
        log = Path(os.path.join(dir_path, base_filename.split('.')[0]+'_log.json'))
        if log.is_file():
            old = ''
            with open(log, 'r') as f:
                try:
                    old = json.loads(f.read())
                except json.decoder.JSONDecodeError:
                    print('There is an error decoding log. Log file may be corrupt')
                    return
            
            should_update = old['checkpoints'][-1]['checkpoint'] != checkpoint
            
            if should_update:
                with open(log, 'w') as f:
                    old["checkpoints"].append({"time":str(datetime.datetime.now()),"checkpoint":checkpoint})
                    f.write(json.dumps(old))
            
        else:
            with open(log, "w") as f:
                new = {"checkpoints":[{"time":str(datetime.datetime.now()),"checkpoint":checkpoint}]}                    
                f.write(json.dumps(new))
    
def start(IRB_consent):
    if IRB_consent:
        print('Consent granted: logging will occur') 
        watch_file = 'A4.ipynb'
        watcher = Watcher(watch_file, logger, base_filename=watch_file)
        thread = threading.Thread(target=lambda: watcher.watch(), daemon=True)
        thread.start()
    else:
        print('Please give consent to logging data by updating agreement variable to True')
        
def compress_log():
    base_filename = 'A4.ipynb'
    src_path = os.path.realpath(base_filename)
    dir_path = os.path.dirname(src_path)
    log = Path(os.path.join(dir_path, base_filename.split('.')[0]+'_log.json'))
    if log.is_file():  
        log_zip = zipfile.ZipFile('A4_log.compressed', 'w')
        log_zip.write(log, base_filename.split('.')[0]+'_log.json', compress_type=zipfile.ZIP_DEFLATED)
        log_zip.close()
        print('Compressed log to: ' + str(os.path.join(dir_path, 'A4_log.compressed')))
    else:
        print('Log file not found. Nothing to compress.')