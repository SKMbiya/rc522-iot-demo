"""
Main module of the demonstrator application
"""
import rc522_iot
import BlynkLib

# Create a blynk object and authenticate communication with the Blynk IoT cloud server. The user needs to enter their 32 character long authentication code sent from Blynk
blynk = BlynkLib.Blynk('################################')

# Create an object of the API
rc522 = rc522_iot.rc522_iot() 

#Checks if EnableSPI button is on or off
spiPin = 2
@blynk.VIRTUAL_WRITE(2)
def EnableSPI(value):
	"""Checks whether SPI is enabled on virtual pin 2  (spiPin) on the client-side application i.e the mobile application to start the communication with RFID card reader 

	Keyword arguments:
	value -- the value sent on from the application, either O or 1, when the button assigned to Blynk's virtual pin 2 is toggled. 
	If value = 1: SPI communication starts, else if O SPI communication is disabled

	spiPin -- the blynk virtual pin (pin 2) assigned to SPI button in the application
	"""
	#If SPI is enabled then program is running
	#Buttons can be pressed
	#Functions are available
	if value==[u'1']:
		rc522.SPICommunication(1)
		blynk.virtual_write(10,"SPI On") #The user is informed that SPI is on

		readPin = 0
		#Handler for GetNameAndIDButton
		@blynk.VIRTUAL_WRITE(0)	
		def GetNameAndID(value):
			"""Prints to the screen the data read from the card, after displaying a prompt message to the user to tap their tag on the card reader

			Keyword arguments:
			value -- the value sent on from the application , either O or 1, when the button assigned to Blynk's virtual pin 0 is clicked.
			If value = 1: the application displays a prompt message, the data read from card is returned to the screen

			readPin -- the blynk virtual pin assigned (pin 0) to NameAndID button in the application

			promptPin -- the blynk virtual pin assigned (pin 10) to the label display component in the application 
			"""
			promptPin = 10
			if value==[u'1']: #If Button is on
				blynk.virtual_write(10,"Tap tag to get ID and name")
				text = rc522.getTextAndID() #ID and name are retrieved 
				blynk.virtual_write(10,text) #ID and name are printed on screen
				blynk.virtual_write(0,0) #Button is switched off

		addMemberPin = 1
		#Handler for Adding a New Member button
		@blynk.VIRTUAL_WRITE(1)
		def AddMember(value):
			"""Writes data to the card, after displaying a prompt message to the user to tap their tag on the card reader and to input the data that needs to be written to the card.
			The user is then notified that data has been written

			Keyword arguments:
			value -- the value sent on from the application , either O or 1, when the button assigned to Blynk's virtual pin 1 is clicked.
			If value = 1: the application displays prompt message, the read id and text from card are returned to the screen

			promptPin -- the blynk virtual pin assigned (pin 10) to the label display component in the application 

			ReadInput(str) -- is a method which handles the blynk input stream via the Text Field component used in the application. 
			"""
			if value==[u'1']: #If button is on
				blynk.virtual_write(10,"Type name of person to add:")

				textFieldPin = 9
				promptPin = 10
				#Handler for input stream in Blynk
				@blynk.VIRTUAL_WRITE(9)
				def ReadInput(str):
					"""Handles the reading of the users input in the TextField component

					Keyword arguments:
						str -- is the string data that the user inputs to the Text Field component

						textFieldPin -- the blynk virtual pin assigned (pin 9) to the text field component in the application 
					"""
					text = ' '.join(str) #Input is received as array and converted to string
					blynk.virtual_write(10,"Tap tag")
					name = rc522.WriteToCard(text) #Input is sent to be written to card
					blynk.virtual_write(10,"Added the member "+name) #User is notified that card is written to
					blynk.virtual_write(1,0) #Button is turned off
		
		resetPin = 3
		#Handler for Resetting card information
		@blynk.VIRTUAL_WRITE(3)
		def Reset(value):
			"""Resets (or clears) the data that is stored on the cards, after prompting the user to tap their card to be clear

			Keyword arguments:
			value -- the value sent on from the application , either O or 1, when the button assigned to Blynk's virtual pin 3 is clicked.
			If value = 1: the application displays prompt message and the user's card is cleared. The user then is notified that their data has been reset

			resetPin -- the blynk virtual pin assigned (pin 3) to Reset button in the application

			promptPin -- the blynk virtual pin assigned (pin 10) to the label display component in the application 
			"""
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
