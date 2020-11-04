"""Main module."""
import rc522_iot
import BlynkLib

# Initialize Blynk
blynk = BlynkLib.Blynk('################################')

rc522 = rc522_iot.rc522_iot() #Create object of API

#Checks if EnableSPI button is on or off
@blynk.VIRTUAL_WRITE(2)
def EnableSPI(value):
	#If SPI is enabled then program is running
	#Buttons can be pressed
	#Functions are available
	if value==[u'1']:
		rc522.SPICommunication(1)
		blynk.virtual_write(10,"SPI On") #The user is informed that SPI is on

		#Handler for GetNameAndIDButton
		@blynk.VIRTUAL_WRITE(0)	
		def GetNameAndID(value):
			if value==[u'1']: #If Button is on
				blynk.virtual_write(10,"Tap tag to get ID and name")
				text = rc522.getTextAndID() #ID and name are retrieved 
				blynk.virtual_write(10,text) #ID and name are printed on screen
				blynk.virtual_write(0,0) #Button is switched off
		#Handler for Adding a New Member button
		@blynk.VIRTUAL_WRITE(1)
		def AddMember(value):
			if value==[u'1']: #If button is on
				blynk.virtual_write(10,"Type name of person to add:")

				#Handler for input stream in Blynk
				@blynk.VIRTUAL_WRITE(9)
				def ReadInput(str):
					text = ' '.join(str) #Input is received as array and converted to string
					blynk.virtual_write(10,"Tap tag")
					name = rc522.WriteToCard(text) #Input is sent to be written to card
					blynk.virtual_write(10,"Added the member "+name) #User is notified that card is written to
					blynk.virtual_write(1,0) #Button is turned off
		#Handler for Resetting card information
		@blynk.VIRTUAL_WRITE(3)
		def Reset(value):
			if value==[u'1']: #If Reset button is pressed
				rc522.Reset(1) #API resets the data on the card
				blynk.virtual_write(10,"The id has been reset") #User is notified
				blynk.virtual_write(3,0) #Button is turned off
			elif value==[u'0']:
				blynk.virtual_write(10,rc522.Reset(0))

	elif value==[u'0']: #If button for SPI is off
		rc522.SPICommunication(0) #API communication is disabled
		blynk.virtual_write(10,"SPI Off")
while True:
	blynk.run()
