### -------------------------------------------------------------------------------------------------------------------
### .docx / .doc ==> .pdf in termincal bc microsoft word actually takes two hundred millennium to start up
### -------------------------------------------------------------------------------------------------------------------


import glob, os, sys, win32com.client, comtypes.client, time


cwd = r'C:\Users\brian\Desktop\RAM'
os.chdir(cwd)

print('~~~Convert Word to Pdf~~~')


for fullFileName in glob.glob("*.docx") + glob.glob("*.doc"):

	fileName = fullFileName.split('.')[0]
	fileType = fullFileName.split('.')[1]

	word = win32com.client.Dispatch('Word.Application')
	doc = word.Documents.Open(os.path.join(cwd, fullFileName))
	doc.SaveAs(os.path.join(cwd, fileName + '.pdf'), FileFormat = 17)

	doc.Close()
	word.Quit()
	print('Converted to PDF: ' + fileName + '.pdf')

	time.sleep(.1)

cwd = r'D:\Files\Courses\RAM'
os.chdir(cwd)



for fullFileName in glob.glob("*.docx") + glob.glob("*.doc"):

	fileName = fullFileName.split('.')[0]
	fileType = fullFileName.split('.')[1]

	word = win32com.client.Dispatch('Word.Application')
	doc = word.Documents.Open(os.path.join(cwd, fullFileName))
	doc.SaveAs(os.path.join(cwd, fileName + '.pdf'), FileFormat = 17)

	doc.Close()
	word.Quit()
	print('Converted to PDF: ' + fileName + '.pdf')

	time.sleep(.1)
    