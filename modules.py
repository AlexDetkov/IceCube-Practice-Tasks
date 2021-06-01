from icecube import icetray, dataclasses, simclasses, recclasses

class NhitModule(icetray.I3Module):
	def __init__(self, context):
		icetray.I3Module.__init__(self, context)
		self.AddParameter("Results", "location to return results", None)
	
	def Configure(self):
		self.results = self.GetParameter("Results")
	
	def Physics(self, frame):
		if frame.Has("CVMultiplicity"):
			hits = frame.Get("CVMultiplicity").n_hit_doms
			self.results.append(hits)
		self.PushFrame(frame)
		

class NhitEnergyModule(icetray.I3Module):
	def __init__(self, context):
		icetray.I3Module.__init__(self, context)
		self.AddParameter("Results", "location to return results", None)
	
	def Configure(self):
		self.results = self.GetParameter("Results")
		
	def Physics(self, frame):
		if frame.Has("CVMultiplicity") and frame.Has("CVStatistics"):
			hits = frame.Get("CVMultiplicity").n_hit_doms
			q = frame.Get("CVStatistics").q_tot_pulses
			self.results.append([hits, q])
		self.PushFrame(frame)
		
		
class LineFitDCZenith(icetray.I3Module):
	def __init__(self, context):
		icetray.I3Module.__init__(self, context)
		self.AddParameter("Results", "location to return results", None)
	
	def Configure(self):
		self.results = self.GetParameter("Results")
		
	def Physics(self, frame):
		if frame.Has("LineFit_DC"):
			zenith = frame.Get("LineFit_DC").dir.zenith
			self.results.append(zenith)
		self.PushFrame(frame)
		
class LineFitZenith(icetray.I3Module):
	def __init__(self, context):
		icetray.I3Module.__init__(self, context)
		self.AddParameter("Results", "location to return results", None)
	
	def Configure(self):
		self.results = self.GetParameter("Results")
		
	def Physics(self, frame):
		if frame.Has("LineFit"):
			zenith = frame.Get("LineFit").dir.zenith
			self.results.append(zenith)
		self.PushFrame(frame)
