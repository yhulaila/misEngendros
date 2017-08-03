#/usr/bin/python

####################################################################################
#                                                                                  #
#                                SpiceSync Utility v1                              #
#                                                                                  #
####################################################################################

# This utility is designed to download SPICE kernels based on a metakernel provided.
# It has a config file, spicesync.ini that contains all the neccessary paths and
# variables to specify prior to launch.
#
# Once launched, it:
#   - downloads the metakernel from SPICE FTP
#   - generates a list of kernel files mentioned in it
#   - syncs from remote to local only files mentioned in metakernel with the server, 
#     comparing modification time and size
#
# Based on settings set in the .ini file, it can also:
#   - purge the local SPICE directory before work
#   - edit the metakernel locally to add the local path to PATH_VALUES
#   - log activities on debug or info level
#
# The following python libraries are required: 
#   - configparser
#   - ftplib
#   - ftputil
#   - urllib
#   - os
#   - re
#   - logging
# They must be installed in python (with pip or other tool)
#
# Changelog at the end of this file.

def readConfig(path):
    import configparser

    config = configparser.ConfigParser()
    config.read(path)

    return config

def getMK(server, serverPath):
    from ftplib import FTP
    from urllib.parse import urlparse
    import os.path
    print ('estoy dentro')
    try:
        ftp = FTP(urlparse(server).netloc)
        ftp.login()
        ftp.cwd(urlparse(server).path+os.path.dirname(serverPath))

        lines = []
        ftp.retrlines('RETR '+os.path.split(serverPath)[1], lines.append)

        logging.info("Success fetching %s with %d lines in it", serverPath, len(lines))
        print (lines)
        return lines
    except BaseException:
        logging.exception("Could not download MK file")
        return 0

def parseFileList(lines):
    import re
    
    try:
        m = re.search(r"PATH_SYMBOLS += +\( +\'(.+)\' +\)", lines)
        files = re.findall(r"\'\$"+m.group(1)+r"\/(.+?)\'", lines)

        logging.info("Metakernel parsed, %d kernel files found", len(files))
        print (files)
        return files
    except BaseException:
        logging.exception("Could not parse MK file")
        return 0

def doSync(fileList, localPath, remotePath):
    from urllib.parse import urlparse
    from ftputil.host import FTPHost
    import os

    logging.info("Start Syncing from %s to %s", remotePath, localPath)

    count = 0

    try:
        #create neccessary dirs
        dirs = []
        for file in fileList:
            if (os.path.dirname(file) not in dirs):
                dirs.append(os.path.dirname(file))
                if (not os.path.exists(localPath+dirs[-1])):
                    os.mkdir(localPath+dirs[-1])
    
        ftp = FTPHost(urlparse(remotePath).netloc, "anonymous")
        for file in fileList:
            rFile = urlparse(remotePath).path+file
            lFile = localPath+file
            logging.debug("Processing %s", rFile)
            if ftp.path.exists(rFile):
                rStat = ftp.lstat(rFile)
                if os.path.exists(lFile):
                    lStat = os.stat(lFile)
                    if (rStat[os.path.stat.ST_MTIME] > lStat[os.path.stat.ST_MTIME] or rStat[os.path.stat.ST_SIZE] != lStat[os.path.stat.ST_SIZE]):
                        ftp.download(rFile, lFile)
                        os.utime(lFile, (int(rStat[os.path.stat.ST_MTIME]), int(rStat[os.path.stat.ST_MTIME])))
                        logging.debug("Updated %s locally, a change compared with server detected", lFile)
                        count += 1
                    else:
                        logging.debug("Local file %s up to date", lFile)
                else:
                    ftp.download(rFile, lFile)
                    os.utime(lFile, (int(rStat[os.path.stat.ST_MTIME]), int(rStat[os.path.stat.ST_MTIME])))
                    logging.debug("Downloaded %s no such file found locally", rFile)
                    count += 1
            else:
                logging.error("%s not found on server", rFile)

        logging.info("Done syncing. %d files updated locally.", count)
        print ("Done syncing. %d files updated locally.", count)
        return 1
    except BaseException:
        logging.exception("Could not sync the files on a list")
        return 0

def updateMK(destDir, kernel):

    logging.info("Updating MK with the local dir variable")

    try:
        fp = open(destDir+kernel, 'r')
        lines = fp.read()
        fp.close()
    
        import re, os
        a = destDir.rstrip(os.sep)
        if '\\\\' in destDir:
            a = re.escape(a)
        lines = re.sub(r"(PATH_VALUES += +\( +\')(..)(\' +\))", r"\1"+a+r"\3", lines)

        fp = open(destDir+kernel, 'w')
        fp.write(lines)
        fp.close()   
    except BaseException:
        logging.exception("Could not sync the files on a list")
        return 0

    return 1

import sys
config_file = 'spicesync.ini'
configs = readConfig(config_file)

#Setup logging
import logging
logging.basicConfig(filename=configs['LOCAL']['WorkDir']+'spicesync.log',
format='%(asctime)s [%(levelname)s] in %(funcName)s: %(message)s',
datefmt='%Y-%m-%d %H:%M:%S', level=int(configs['LOCAL']['LogLevel']))
logging.info("Starting SpiceSync")

#Purge directories if needed
if configs['LOCAL']['Purge'] == '1' :
    import shutil, os
    shutil.rmtree(configs['LOCAL']['DestDir'])
    os.mkdir(configs['LOCAL']['DestDir'])
    logging.info("Purged %s", configs['LOCAL']['DestDir'])

#Get metakernel files list for download
files = getMK(configs['SERVER']['SpiceFTP'], configs['SERVER']['kernel'])
if files == 0:
    logging.error("Quitting due to errors during getMK()")
    exit(0)

#Parsing MK file to list
files = ';'.join(files)
files = parseFileList(files)
if files == 0:
    logging.error("Quitting due to errors during parseFileList()")
    exit(0)
#add mk file itself to filelist
files.append(configs['SERVER']['kernel'])

#Finally sync the files
ret = doSync(files, configs['LOCAL']['DestDir'], configs['SERVER']['SpiceFTP'])
if ret == 0:
    logging.error("Quitting due to errors during doSync()")
    exit(0)

#Edit MK if needed
ret = updateMK(configs['LOCAL']['DestDir'],configs['SERVER']['kernel'])
if ret == 0:
    logging.error("Could not update the MK.")

logging.info("Execution complete\n")
logging.shutdown()
exit(0)

####################################################################################
#                                                                                  #
#                                      CHANGELOG                                   #
#                                                                                  #
####################################################################################

# v1 2017-02-08 First Release

# v2 2017-03-06 defined spicesync as a function with the config file as in input

getMK(server, serverPath)
parseFileList(lines)
doSync(fileList, localPath, remotePath)
updateMK(destDir, kernel)