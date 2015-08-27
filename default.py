# X10-Light - Service
"""
    Document   : default.py
    Package    : X10 Commander Lights
    Author     : Majestic Soft
    Copyright  : 2011, Majestic Soft, NL
    License    : Gnu General Public License - see LICENSE.TXT
    Description: General control code for X10 Commander Lights
    Revision   : 0.0.3
                 Added: this descriptive text
                 Added: HomeSeer control via tenHsServer (http://www.tenholder.net/tenWare2/tenHsServer/default.aspx)
"""
# IMPORT LIBRARIES
import sys
import os
import subprocess
import xbmc
import xbmcgui
import xbmcaddon
import urllib2
import socket
import time
from socket import *

xbmc.log('My Home: ******************* X10-Light *******************')
xbmc.log('My Home: Import of libraries is done')
xbmc.log('My Home: *************************************************')

# ADDON INFORMATION
__addon__     = xbmcaddon.Addon()
__addonname__ = __addon__.getAddonInfo('name')
__cwd__       = __addon__.getAddonInfo('path')
__author__    = __addon__.getAddonInfo('author')
__version__   = __addon__.getAddonInfo('version')
xbmc.log('My Home: *************** Addon information ***************')
xbmc.log('My Home: Addon info name    : ' + __addonname__)
xbmc.log('My Home: Addon info path    : ' + __cwd__)
xbmc.log('My Home: Addon info author  : ' + __author__ )
xbmc.log('My Home: Addon info version : ' + __version__)
xbmc.log('My Home: *************************************************')
xbmc.log('My Home: Addon information is read and shown in log file')

# ADDON HOST SETTINGS
my_ip = __addon__.getSetting("IP")
my_port = __addon__.getSetting("PORT")

# ADDON LIST SET

myhomewhat = []
myhomewho = []
for i in range(0, 101):
	myhomewhat.append('11')
	myhomewho.append('11')

		
xbmc.log('My Home: *************** Addon Host settings *************')
xbmc.log('My Home: IP number          : ' + my_ip)
xbmc.log('My Home: PORT number        : ' + my_port)


# ADDON START
#START Initialisation cycle
#Make sure Device is on
#xbmc.log('My Home: *************************************************')

# ADDON PLAYER
xbmc.log('My Home: ****************** CLASS PLAYER *****************')

def invia2(cmdopen):
	xbmc.log("My Home: " + cmdopen)



def invia(cmdopen):
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((my_ip, int(my_port)))
    client.send(cmdopen)
    client.close
	
def scenario(inizio,fine):
		for i in range(inizio, fine):
			myhomewhat.insert( i , __addon__.getSetting(str(i)))
			myhomewho.insert( i , __addon__.getSetting(str(i) + "address"))
			if myhomewhat[i] == "11":
				xbmc.log("Contatore " + str(i) + " non fare nulla")
			else:
				xbmc.log (str(i) + " - Messaggio Open - Contatore " +  "*1*" + myhomewhat[i] +"*" + myhomewho[i] + "##")
				invia("*1*" + myhomewhat[i] +"*" + myhomewho[i] + "##")

				
class MyPlayer(xbmc.Player) :
    xbmc.log('My Home: Class player is opened')
    
    def __init__ (self):
		xbmc.Player.__init__(self)
		scenario(1,11)
		xbmc.log('My Home: Class player is initialized')
		
        
    def onPlayBackStarted(self):
        if xbmc.Player().isPlayingVideo():
			scenario(21,31)
			xbmc.log('My Home: PLAYBACK STARTED')
            #Execute Player START Event settings on Device
            
    def onPlayBackEnded(self):
        if (VIDEO == 1):
			scenario(61,71)
			xbmc.log('My Home: PLAYBACK ENDED')
            #Execute Player END Event settings on Device
            
    def onPlayBackStopped(self):
        if (VIDEO == 1):
			scenario(31,41)
			xbmc.log('My Home: PLAYBACK STOPPED')
            #Execute Player STOP Event settings on Device
            
    def onPlayBackPaused(self):
        if xbmc.Player().isPlayingVideo():
			scenario(41,51)
			xbmc.log('My Home: PLAYBACK PAUSED')
			#Execute Player PAUSE Event settings on Device
            
    def onPlayBackResumed(self):
        if xbmc.Player().isPlayingVideo():
			scenario(51,61)
			xbmc.log('My Home: PLAYBACK RESUMED')
            
player=MyPlayer()

while (not xbmc.abortRequested):
    if xbmc.Player().isPlayingVideo():
        VIDEO = 1
    else:
        VIDEO = 0

    xbmc.sleep(1000)

while (xbmc.abortRequested):
    #Execute XBMC STOP Event settings on Device
	scenario(11,21)
	xbmc.log('My Home: Switch lights off')

xbmc.log('My Home: *************************************************')