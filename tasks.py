from I3Tray import I3Tray
from icecube import icetray, dataclasses, dataio
from modules import *
import ROOT
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt

#################################################################################################################
# Variables													#
#################################################################################################################

NumberHits = []
NhitEnergy = []
Zenith = []

#################################################################################################################
# Ice Tray													#
#################################################################################################################

tray = I3Tray()
tray.Add('I3Reader', Filename='/data/icecube/testfiles/testfile.i3.zst')
tray.Add(NhitModule, Results=NumberHits)
tray.Add(NhitEnergyModule, Results=NhitEnergy)
tray.Add(LineFitDCZenith, Results=Zenith)
tray.Execute(27) # how to go to completion or get number of frames
tray.Finish()

#################################################################################################################
# Nhits Histogram												#
#################################################################################################################

n, bins, _ = plt.hist(NumberHits, bins="auto", label="Data")
plt.xlabel('NHits')
plt.ylabel('Frequency')
plt.title('Histogram of NHits')
plt.savefig('output/Nhits_Histogram.png')
plt.clf()

#################################################################################################################
# Nhits vs Energy Correlation											#
#################################################################################################################

x, y = zip(*NhitEnergy)
plt.scatter(x, y)
plt.xlabel('NHits')
plt.ylabel('Energy')
plt.title('Nhits vs Energy Correlation')
plt.savefig('output/Nhits_vs_Energy_Scatter.png')
plt.clf()


plt.hist2d(x, y, cmap=plt.cm.Greys)
plt.xlabel('NHits')
plt.ylabel('Energy')
plt.title('Nhits vs Energy Correlation')
plt.colorbar()
plt.savefig('output/Nhits_vs_Energy_Histogram.png')
plt.clf()

#################################################################################################################
# Zenith Histogram												#
#################################################################################################################

n, bins, _ = plt.hist(Zenith, bins="auto", label="Data")
plt.xlabel('NHits')
plt.ylabel('Frequency')
plt.title('Histogram of Zenith')
plt.savefig('output/Zenith_Histogram.png')
plt.clf()

#################################################################################################################
# Zenith Error vs 											#
#################################################################################################################

