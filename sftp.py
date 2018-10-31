# coding=utf-8
# 
# Upload files to a sftp site. The code comes recon_helper package, with
# minor modifications.
# 
# This script calls the program WinSCP to do that upload, so make sure WinSCP
# is installed. Because WinSCP uses SSH, please use WinSCP to manually connect
# to a site to make sure the public keys are accepted.
# 

from datetime import datetime
from os.path import join
from subprocess import run, TimeoutExpired, CalledProcessError
import logging
logger = logging.getLogger(__name__)



class UploadError(Exception):
	pass



def upload(files, config):
	"""
	[List] files, [Dictionary] config => upload files to the target ftp site.

	The config object stores the following information:

	winscpPath: the full path to the WinSCP.com executable
	timeout: the time out setting (in seconds)
	scriptDir: the directory to store winscp scripts.
	logDir: the directory to store winscp logs.

	user: the user name to login to ftp server
	password: the password to login to ftp server
	server: the URL of the server
	targetDir: the directory to upload files to
	"""
	winscpLog = createLog(config['logDir'])
	args = [config['winscpPath'], 
			'/script={0}'.format(createScript(files, config)),
			'/log={0}'.format(winscpLog)]

	# Invoke WinSCP as a subprocess to do the upload
	result = run(args, timeout=config['timeout'], check=True)

	if len(files) != countSuccess(winscpLog):
		logger.error('upload(): {0} files, {1} succeeded'.format(len(files), countSuccess(winscp_log)))
		raise UploadError()



def getTimeStamp():
	return datetime.now().strftime('%Y%m%dT%H%M%S')



def createScript(files, config):
	"""
	[List] files, [Dictionary] config => [String] script file name

	Create a script file to be loaded by WinSCP.com, a sample file looks like:

	open sftp://demo:password@test.rebex.net/
	cd pub/example
	get ConsoleClient.png
	exit
	"""
	scriptFile = join(config['scriptDir'], 'run-sftp_{0}.txt'.format(getTimeStamp()))
	with open(scriptFile, 'w') as f:
		f.write('open sftp://{0}:{1}@{2}\n'.\
				format(config['user'], config['password'], config['server']))

		f.write('cd {0}\n'.format(config['targetDir']))
		for file in files:
			f.write('put {0}\n'.format(file))

		f.write('exit')

	return scriptFile



def createLog(logDir):
	"""
	[String] logDir => [String] log file name

	Create an empty log file in logDir, because winscp.com needs an existing log
	file to start logging.
	"""
	logFile = join(logDir, 'log_{0}.txt'.format(getTimeStamp()))
	with open(logFile, 'w') as f:	# just create an empty file
		pass

	return logFile



def countSuccess(winscp_log):
	"""
	Look for successful transfer records in the winscp logfile, then count
	the total number of successful uploads.

	The successful transfer records are in the following format (get and put)

	> 2016-12-29 17:20:40.652 Transfer done: '<file full path>' [xxxx]

	The starting symbol can be '>', '<', '.', '!', depending on the type of
	the record.

	If it is a get, then 'file full path' will be the remote directory's
	file path. If it is a put, then 'file full path' will be the local
	directory's file path.
	"""
	successful_list = []
	with open(winscp_log) as f:
		for line in f:
			tokens = line.split()
			if len(tokens) < 6:
				continue

			if tokens[3] == 'Transfer' and tokens[4] == 'done:':
				successful_list.append(tokens[5][1:-1])

	return len(successful_list)



if __name__ == '__main__':
	"""
	For testing only.
	"""
	# file_list = ['/pub/example/ConsoleClient.png', \
	# 				'/pub/example/FtpDownloader.png', \
	# 				'/pub/example/mail-editor.png']
	file_list = [r'C:\temp2\sample.txt', r'C:\temp2\sample2.txt']
	result = upload(file_list)
	print(result)