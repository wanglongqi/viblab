import numpy as np
class UFF58(object):
	def __init__(self):
		pass
	
	def readuff(self,fid):
		if not type(fid)==file:
			fid=open(fid)
		print fid.readline().strip()
		print fid.readline().strip()
		self.id=fid.readline()+fid.readline()+fid.readline()+fid.readline()+fid.readline()
		line=fid.readline().split()
		self.FunctionType=int(line[0])
		self.FunctionID=int(line[1])
		self.VersionNumber=int(line[2])
		self.LoadCaseID=int(line[3])
		self.ResponseEntityName=line[4].strip()
		self.ResponseNode=int(line[5])
		self.ResponseDirection=int(line[6])
		self.ReferenceEntityName=line[7].strip()
		self.ReferenceNode=int(line[8])
		self.ReferenceDirection=int(line[9])
		line=fid.readline().split()
		self.OrdinateDataType=int(line[0])
		self.NumberofUnevenData=int(line[1])
		self.AbscissaSpacing=int(line[2])
		self.AbscissaMinimum=float(line[3])
		self.AbscissaIncrement=float(line[4])
		self.ZAxisValue=float(line[5])
		line=fid.readline().split()
		self.R8SpecificDataType=int(line[0])
		self.R8LengthUnitExp=int(line[1])
		self.R8ForceUnitExp=int(line[2])
		self.R8TemperatureUnitExp=int(line[3])
		self.R8AxisLabel=line[4].strip()
		self.R8AxisUnitLabel=line[5].strip()		
		line=fid.readline().split()
		self.R9SpecificDataType=int(line[0])
		self.R9LengthUnitExp=int(line[1])
		self.R9ForceUnitExp=int(line[2])
		self.R9TemperatureUnitExp=int(line[3])
		self.R9AxisLabel=line[4].strip()
		self.R9AxisUnitLabel=line[5].strip()	
		line=fid.readline().split()
		self.R10SpecificDataType=int(line[0])
		self.R10LengthUnitExp=int(line[1])
		self.R10ForceUnitExp=int(line[2])
		self.R10TemperatureUnitExp=int(line[3])
		self.R10AxisLabel=line[4].strip()
		self.R10AxisUnitLabel=line[5].strip()
		line=fid.readline().split()
		self.R11SpecificDataType=int(line[0])
		self.R11LengthUnitExp=int(line[1])
		self.R11ForceUnitExp=int(line[2])
		self.R11TemperatureUnitExp=int(line[3])
		self.R11AxisLabel=line[4].strip()
		self.R11AxisUnitLabel=line[5].strip()
		dtype={2 :np.float32,
				4 :np.float64,
				5 :np.complex64,
				6 :np.complex128}
		self.Data=np.fromfile(fid,dtype=dtype[self.OrdinateDataType],count=self.NumberofUnevenData)

		
	
	
	