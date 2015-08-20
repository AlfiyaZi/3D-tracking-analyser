from __init__ import *
import csv



class ChooseColumnsWindow(BaseWidget):
	
	def __init__(self):
		super(ChooseColumnsWindow,self).__init__('CSV Choose the columns')
		self._filename = None

		#Definition of the forms fields
		self._filename = ControlFile('File')
		self._separator = ControlText('Separator', ';')
		self._frameCol = ControlNumber('Frame column', 0, 0, 100)
		self._xCol = ControlNumber('X column', 1, 0, 100)
		self._yCol = ControlNumber('Y column', 2, 0, 100)
		self._zCol 	= ControlNumber('Z column', 3, 0, 100)
		self._filePreview = ControlList('Preview')
		self._loadButton = ControlButton('Load')

		self._formset = [ '_filename',('_separator','_frameCol', '_xCol', '_yCol','_zCol','_loadButton'), '_filePreview' ]
		self._separator.changed = self.__refreshPreview
		self._filename.changed = self.__refreshPreview

		self._filename.value = '/home/ricardo/Downloads/2012.12.01_13.48_3D_POSITIONS_version_03.06.2015.csv'

		
	@property
	def filename(self): return self._filename.value

	@filename.setter
	def filename(self, value):
		self._filename.value = value
		self.__refreshPreview()
	

	@property
	def loadFileEvent(self): return self._loadButton.value

	@loadFileEvent.setter
	def loadFileEvent(self, value): self._loadButton.value = value
	

	@property
	def separator(self): return self._separator.value

	@property
	def frameColumn(self): return self._frameCol.value

	@property
	def xColumn(self): return self._xCol.value

	@property
	def yColumn(self): return self._yCol.value

	@property
	def zColumn(self): return self._zCol.value

	



	def __refreshPreview(self):
		if self._filename.value!=None and self._filename.value!='':
			with open(self._filename.value) as csvfile:
				spamreader = csv.reader(csvfile, delimiter=self._separator.value)
				self._filePreview.value = []
				self._filePreview.horizontalHeaders = ["0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16",]
				for i, row in enumerate(spamreader):
					self._filePreview += row
					if i>=10: break

##################################################################################################################
##################################################################################################################
##################################################################################################################

#Execute the application
if __name__ == "__main__":	 app.startApp( ChooseColumnsWindow )