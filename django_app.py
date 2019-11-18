#!/usr/bin/python
import sys
import os
import subprocess
import datetime


class django():

    def __init__(self):
        '''dummy initialize'''
        self.server_path = "."
        self.server_folder_name = "upload_download_file_server_app"
        self.server_app_name = "upload_download_file_server_app"
        self.port = "8800"
        self.python_version = "python2.7"

    def DoError (self,Error) :
        sys.stderr.write(Error)
        sys.exit(1)

    def executeCommand(self,cmd_to_execute):
        '''
        Execute the bash command
        '''
        try:
            check_state = subprocess.Popen(cmd_to_execute, shell=True,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            executable = "/bin/bash")
            output, error = check_state.communicate()
            return check_state.returncode, output, error
        except Exception as e:
            self.DoError(str(e))

    def start_gunicorn(self):
        try:
            command_to_start_gunicorn = "cd "+self.server_path+";source ./venv/bin/activate &&\
                                             cd "+self.server_folder_name+" && \
                                             gunicorn --bind 0.0.0.0:"+self.port+" \
                                                 "+self.server_app_name+".wsgi:application \
                                                     --daemon --access-logfile access.log \
                                                         --error-logfile error.log"
            pid_returncode, pid_output, pid_error = self.executeCommand(command_to_start_gunicorn)
            if pid_returncode == 0 :
                print("Succefully started the web server" )
            else:
                print("Problem with starting the web server")
        except Exception as e:
            self.DoError(str(e))

    def stop_gunicorn(self):
        try:
            command_to_get_gunicorn_pid = "ps -ef | grep gunicorn | grep "+self.port+" | grep -v grep | awk '{print $2}'"
            pid_returncode, pid_output, pid_error = self.executeCommand(command_to_get_gunicorn_pid)
            if pid_returncode == 0 and pid_output:
                pid_output_list = pid_output.strip().split("\n")
                for temp_pid in pid_output_list:
                    command_kill_pid = "kill -9 " + temp_pid.strip()
                    pid_returncode, pid_output, pid_error = self.executeCommand(command_kill_pid)
                    if pid_returncode == 0:
                        print("Succefully killed the pid : " + temp_pid )
                    else:
                        print("Unsuccefull in the killing the pid : " + temp_pid )
                print("Succefully stopped the process")
            else:
                print("No process to kill")
        except Exception as e:
            self.DoError(str(e))

    def install_virtualenv_django(self):
        try:
            command_to_install_virtualenv = "virtualenv venv -p " +  self.python_version
            pid_returncode, pid_output, pid_error = self.executeCommand(command_to_install_virtualenv)
            if pid_returncode == 0:
                command_to_install_django = "source ./venv/bin/activate && pip install django"
                pid_returncode, pid_output, pid_error = self.executeCommand(command_to_install_django)
                if pid_returncode == 0:
                    command_to_install_gunicorn = "source ./venv/bin/activate && pip install gunicorn"
                    pid_returncode, pid_output, pid_error = self.executeCommand(command_to_install_gunicorn)
                    if pid_returncode == 0:
                        print("Succefully created virutal env and installed django and gunicorn")
                    else:
                        print("Unsuccefull in installing gunicorn in virtualenv" )
                else:
                    print("Unsuccefull in installing django in virtualenv" )
            else:
                print("virtualenv is not installed in you environment, please install using 'pip install virtualenv'")
        except Exception as e:
            self.DoError(str(e))

    def main(self):
        try:
            if len(sys.argv) == 2:
                user_input = sys.argv[1] # --start --stop
                if user_input == "--start":
                    self.start_gunicorn()
                elif user_input == "--stop":
                    self.stop_gunicorn()
                elif user_input == "--install":
                    self.install_virtualenv_django()
                else:
                    print("Please execute as below")
                    print("Ex: ./django_app.py --start/--stop/--install")                 
            else:
                print("Please execute as below") 
                print("Ex: ./django_app.py --start/--stop/--install")                 
        except Exception as e:
            print("Please execute as below") 
            print("Ex: ./django_app.py --start/--stop/--install")                 


if __name__ == '__main__':
    ob = django()
    ob.main()
