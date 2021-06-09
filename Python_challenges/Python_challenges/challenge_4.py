import psutil
import csv


def main():
    fields = ['Name','ID','Memory Utilization']
    filename = 'processes.csv'

    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
    
        csvwriter.writerow(fields)
    
    
        for proc in psutil.process_iter():
            try:
            # Get process name,pid, and Memory utilization from process object.
                processName = proc.name()
                processID = proc.pid
                processMemory = proc.memory_percent()
            
            
                rows = [[processName, processID,processMemory]]
            
            
                csvwriter.writerows(rows)
                
            
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    
